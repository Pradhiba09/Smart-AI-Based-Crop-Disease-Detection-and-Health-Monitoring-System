from flask import Flask, render_template, request
# try importing tf.keras first, fall back to standalone keras if needed
try:
    from tensorflow.keras.models import load_model
    from tensorflow.keras.preprocessing import image
    import tensorflow as tf
    KERAS_BACKEND = "tensorflow"
except Exception:
    try:
        import keras
        from keras.models import load_model
        from keras.preprocessing import image
        KERAS_BACKEND = "keras"
    except Exception as e:
        print(f"Error importing Keras: {e}")
        exit(1)

from werkzeug.utils import secure_filename
import numpy as np
import os
import json
from disease_info import DISEASE_INFO
from new_crops_guidelines import NEW_CROPS_GUIDELINES
import traceback

app = Flask(__name__)

MODEL_PATH = "model.h5"  # Old crops model (Pepper, Potato, Tomato)
CROP_MODEL_PATH = ".h5"  # New crops model (Apple, Corn, Grape, Wheat, Cucumber)
SAVED_MODEL_PATH = "saved_model"
SAVED_CROP_MODEL_PATH = "saved_crop_model"
UPLOAD_FOLDER = os.path.join("static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

IMG_SIZE = (128, 128)

# Load CLASS_NAMES from class_mapping.json to match the model's training
def load_class_names():
    try:
        with open("class_mapping.json", "r") as f:
            class_mapping = json.load(f)
        # Sort by index to get correct order
        return [class_mapping[str(i)] for i in range(len(class_mapping))]
    except Exception as e:
        print(f"Warning: Could not load class_mapping.json: {e}")
        return list(DISEASE_INFO.keys())

# Load CROP_CLASS_NAMES from class_mapping_crop.json for new crops model
def load_crop_class_names():
    try:
        with open("class_mapping_crop.json", "r") as f:
            class_mapping = json.load(f)
        # Sort by index to get correct order
        return [class_mapping[str(i)] for i in range(len(class_mapping))]
    except Exception as e:
        print(f"Warning: Could not load class_mapping_crop.json: {e}")
        return []

CLASS_NAMES = load_class_names()
CROP_CLASS_NAMES = load_crop_class_names()

# DEBUG: Print loaded class names at startup
print(f"\n📊 Class Names Loaded:")
print(f"   CLASS_NAMES: {len(CLASS_NAMES)} classes")
print(f"   CROP_CLASS_NAMES: {len(CROP_CLASS_NAMES)} classes")

# derive available crops from both DISEASE_INFO (old crops) and NEW_CROPS_GUIDELINES (new crops)
all_crops = set()
for info in DISEASE_INFO.values():
    all_crops.add(info.get('crop', 'Unknown'))
for info in NEW_CROPS_GUIDELINES.values():
    all_crops.add(info.get('crop', 'Unknown'))
CROPS = sorted(all_crops)


def cleanup_old_uploads():
    """Delete upload files older than 30 days to prevent disk space issues"""
    import time
    upload_dir = "static/uploads"
    if not os.path.exists(upload_dir):
        return
    
    cutoff = time.time() - (30 * 24 * 60 * 60)  # 30 days ago
    cleaned_count = 0
    for filename in os.listdir(upload_dir):
        filepath = os.path.join(upload_dir, filename)
        if os.path.isfile(filepath) and os.path.getmtime(filepath) < cutoff:
            try:
                os.remove(filepath)
                cleaned_count += 1
                print(f"🧹 Cleaned up old upload: {filename}")
            except Exception as e:
                print(f"⚠️  Failed to clean up {filename}: {e}")
    
    if cleaned_count > 0:
        print(f"🧹 Cleanup completed: removed {cleaned_count} old files")


def load_model_safe():
    """Load model from SavedModel (preferred) or Model.h5 (legacy)."""
    # Try SavedModel first (most compatible)
    if os.path.exists(SAVED_MODEL_PATH):
        try:
            model = tf.keras.models.load_model(SAVED_MODEL_PATH)
            print("✓ Loaded old crops model from SavedModel directory")
            return model
        except Exception as e:
            print(f"Warning: SavedModel load failed: {e}")

    # Try Model.h5 as fallback
    if os.path.exists(MODEL_PATH):
        try:
            model = load_model(MODEL_PATH, compile=False)
            print("✓ Loaded old crops model from Model.h5")
            return model
        except Exception as e:
            print(f"Warning: Model.h5 load failed: {e}")

    print("⚠️  No old crops model (model.h5) found.")
    return None


def load_crop_model_safe():
    """Load new crops model from SavedModel or crop.h5."""
    # Try SavedModel first
    if os.path.exists(SAVED_CROP_MODEL_PATH):
        try:
            model = tf.keras.models.load_model(SAVED_CROP_MODEL_PATH)
            print("✓ Loaded new crops model from SavedModel directory")
            return model
        except Exception as e:
            print(f"Warning: SavedModel load failed: {e}")

    # Try crop.h5 as fallback
    if os.path.exists(CROP_MODEL_PATH):
        try:
            model = load_model(CROP_MODEL_PATH, compile=False)
            print("✓ Loaded new crops model from crop.h5")
            return model
        except Exception as e:
            print(f"Warning: crop.h5 load failed: {e}")

    print("⚠️  No new crops model (crop.h5) found.")
    return None


model = load_model_safe()
crop_model = load_crop_model_safe()

# Clean up old uploads at startup to prevent disk space issues
cleanup_old_uploads()


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def predict_disease(img_path, use_crop_model=False):
    """Predict disease using trained model, or return default demo if no model
    
    Args:
        img_path: Path to image file
        use_crop_model: Use crop.h5 (new crops) instead of model.h5 (old crops)
    """
    selected_model = crop_model if use_crop_model else model
    class_names_to_use = CROP_CLASS_NAMES if use_crop_model else CLASS_NAMES
    
    # DEBUG: Print which model and classes are being used
    print(f"\n🔍 DEBUG: use_crop_model={use_crop_model}")
    print(f"🔍 DEBUG: selected_model is None? {selected_model is None}")
    print(f"🔍 DEBUG: Number of class names: {len(class_names_to_use)}")
    print(f"🔍 DEBUG: Class names: {class_names_to_use[:3]}...") # Show first 3
    
    if selected_model is None:
        raise ValueError(
            "Selected model is not loaded. Upload the correct model or choose the matching crop model."
        )

    try:
        # Load image with RGB conversion to handle RGBA and other formats
        img = image.load_img(img_path, target_size=IMG_SIZE, color_mode='rgb')
        x = image.img_to_array(img)
        
        # Ensure pixel values are valid (0-255 range)
        x = np.clip(x, 0, 255)
        
        # Normalize to 0-1 range
        x = x / 255.0
        
        # Add batch dimension
        x = np.expand_dims(x, axis=0)
        
        # Ensure correct dtype
        x = x.astype('float32')
    except Exception as e:
        print(f"Error loading/preprocessing image {img_path}: {e}")
        traceback.print_exc()
        raise ValueError(f"Failed to process image: {str(e)}")

    try:
        preds = selected_model.predict(x)
    except Exception as e:
        print("Error during model.predict:")
        traceback.print_exc()
        # Propagate a clear error to caller by raising
        raise

    # handle both vector and batch outputs
    probs = np.asarray(preds).reshape(-1)
    if probs.size == 0:
        raise ValueError("Model returned empty prediction array")

    # DEBUG: Print prediction info
    print(f"🔍 DEBUG: Model output size: {probs.size}")
    print(f"🔍 DEBUG: Expected class names count: {len(class_names_to_use)}")

    # Validate prediction array size matches number of classes
    if probs.size != len(class_names_to_use):
        # Fallback: if the old model path is actually a crop model, switch maps automatically
        if not use_crop_model and probs.size == len(CROP_CLASS_NAMES):
            print("⚠️  Warning: old crops model returned 19 outputs. Switching to crop class mapping.")
            class_names_to_use = CROP_CLASS_NAMES
        elif use_crop_model and probs.size == len(CLASS_NAMES):
            print("⚠️  Warning: crop model returned 15 outputs. Switching to old class mapping.")
            class_names_to_use = CLASS_NAMES
        else:
            raise ValueError(
                f"Model output size ({probs.size}) doesn't match expected classes ({len(class_names_to_use)}). "
                f"Check that the correct model file is loaded for old vs new crops. Using crop_model={use_crop_model}"
            )

    idx = int(np.argmax(probs))
    # safety: validate index is in valid range
    if idx < 0 or idx >= len(class_names_to_use):
        raise IndexError(f"Invalid class index {idx} (valid range: 0..{len(class_names_to_use)-1})")

    class_name = class_names_to_use[idx]
    confidence = float(probs[idx]) if probs.size > 0 else 0.0
    # return class name and confidence (0.0-1.0)
    return class_name, confidence


def build_prediction_info(class_name, existing_info=None):
    info = dict(existing_info or {})
    label = str(class_name).strip()

    if "___" in label:
        crop_part, disease_part = label.split("___", 1)
        info.setdefault("crop", crop_part.replace("_", " ").title())
        info.setdefault("disease", disease_part.replace("_", " ").title())
    else:
        normalized = label.replace("_", " ").replace("-", " ").strip()
        normalized_lower = normalized.lower()
        matched_crop = None
        for crop in CROPS:
            if crop.lower() in normalized_lower:
                matched_crop = crop
                break

        if matched_crop:
            info.setdefault("crop", matched_crop)
            remainder = normalized_lower.replace(matched_crop.lower(), "").strip()
            if remainder:
                info.setdefault("disease", remainder.title())
            else:
                info.setdefault("disease", "Healthy")
        else:
            info.setdefault("crop", "Unknown Crop")
            info.setdefault("disease", normalized.title())

    info.setdefault(
        "solution",
        info.get("solution", "No detailed guidance available for this prediction.")
    )
    return info


@app.route('/upload_model', methods=['POST'])
def upload_model():
    """Endpoint to upload a trained Keras .h5 model for inference.

    Saves the uploaded file to `MODEL_PATH` or `CROP_MODEL_PATH` based on model_type.
    Returns JSON with success status and message.
    """
    global model, crop_model
    
    # Get which model type is being uploaded
    model_type = request.form.get('model_type', 'old')  # 'old' or 'new'
    
    # Diagnostic logging to help trace upload issues from the client
    try:
        print(f"/upload_model called - model_type={model_type}, content_type={request.content_type}")
        print(f"Incoming files: {list(request.files.keys())}")
    except Exception:
        pass

    file = request.files.get('model')
    if not file or file.filename == '':
        return {"success": False, "message": "No file uploaded."}, 400

    filename = file.filename
    if not (filename.lower().endswith('.h5') or filename.lower().endswith('.hdf5')):
        return {"success": False, "message": "Invalid file type. Upload a .h5 or .hdf5 file."}, 400

    try:
        # Choose correct path based on model type
        save_path = os.path.join('.', CROP_MODEL_PATH if model_type == 'new' else MODEL_PATH)
        file.save(save_path)
        
        # Attempt to reload model
        try:
            new_model = load_model(save_path, compile=False)
            if new_model is None:
                return {"success": False, "message": "Model file is invalid or corrupted."}, 500
            
            # Update the correct model variable
            if model_type == 'new':
                crop_model = new_model
                print(f"✓ Successfully loaded new crops model from {save_path}")
                return {"success": True, "message": "New crops model uploaded and reloaded successfully."}
            else:
                model = new_model
                print(f"✓ Successfully loaded old crops model from {save_path}")
                return {"success": True, "message": "Old crops model uploaded and reloaded successfully."}
        except Exception as load_error:
            return {"success": False, "message": f"Failed to load model: {str(load_error)}"}, 500
    except Exception as e:
        return {"success": False, "message": f"Error saving model: {e}"}, 500


@app.route('/cleanup')
def cleanup_route():
    """Optional manual cleanup endpoint - can be called periodically"""
    cleanup_old_uploads()
    return {"status": "cleanup_completed", "message": "Old upload files cleaned up"}, 200


@app.route('/how-it-works')
def how_it_works():
    """Render the How It Works page explaining the project flow"""
    return render_template("how_it_works.html")


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    info = None
    image_url = None
    error = None
    model_status = "🤖 Using AI Model"  # Default to trained model
    
    if request.method == "POST":
        file = request.files.get("image")
        # Get which model to use (default to old crops model)
        model_choice = request.form.get("model_choice", "old")
        use_crop_model = model_choice == "new"
        
        # DEBUG
        print(f"\n📤 POST Request received")
        print(f"   model_choice from form: '{model_choice}'")
        print(f"   use_crop_model: {use_crop_model}")
        print(f"   crop_model loaded: {crop_model is not None}")
        print(f"   model loaded: {model is not None}")
        
        if file and file.filename and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(save_path)
            try:
                pred = predict_disease(save_path, use_crop_model=use_crop_model)
                if pred:
                    # pred may be (class, confidence)
                    if isinstance(pred, (tuple, list)):
                        class_name, conf = pred[0], float(pred[1])
                    else:
                        class_name, conf = pred, 0.0

                    # Use appropriate guidelines based on model choice
                    if use_crop_model:
                        info = dict(NEW_CROPS_GUIDELINES.get(class_name, {}))
                    else:
                        info = dict(DISEASE_INFO.get(class_name, {}))

                    info = build_prediction_info(class_name, info)

                    print(f"   DEBUG prediction: class_name={class_name}, info_crop={info.get('crop')}, info_disease={info.get('disease')}")
                    result = class_name
                    image_url = os.path.join("uploads", filename)
                    # pass confidence to template via model_status for now
                    model_status = f"🤖 Using AI Model — Confidence: {conf*100:.1f}%"
                else:
                    error = "Could not process image. Try another."
            except Exception as e:
                # Log full traceback and show friendly error
                print("Exception during prediction:")
                traceback.print_exc()
                error = f"Internal prediction error: {str(e)}"
        else:
            error = "Invalid file. Upload a PNG image."

    return render_template("index.html", result=result, info=info, image_url=image_url, error=error, model_status=model_status, crops=CROPS)


if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)
