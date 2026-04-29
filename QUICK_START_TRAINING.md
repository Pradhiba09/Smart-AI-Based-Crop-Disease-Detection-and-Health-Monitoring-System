# 📋 QUICK START - Train Model with 8 Crops

## Your Updated Project: 34 Disease Classes

You now have folder structure ready for **8 crops (34 disease classes)**:

### ✅ Ready to Use
- Pepper Bell (2 diseases)
- Potato (3 diseases)  
- Tomato (7 diseases)

### ⏳ New - Needs Images
- Apple (4 diseases)
- Corn (4 diseases)
- Grape (4 diseases)
- Wheat (4 diseases)
- Cucumber (3 diseases)

---

## Option A: Use Existing PlantVillage Dataset (Easiest)

If you already have PlantVillage dataset with Pepper, Potato, Tomato:

```bash
# Copy/extract existing images to PlantVillage/ folder
# Then retrain model with just those 3 crops

python train_model.py --epochs 10
```

---

## Option B: Add New Crops (Full Setup)

### Step 1️⃣ - Download Images for New Crops

For **Apple, Corn, Grape, Wheat, Cucumber**, get images from:

- **Google Images** (50-100 images each disease)
  - Search: "apple scab disease leaves"
  - Save to: `PlantVillage/Apple___Apple_scab/`

- **Kaggle Datasets**
  - Search crop disease datasets
  - Extract to PlantVillage/

- **Your Photos**
  - Take pictures of diseased plants
  - Organize into folders: `PlantVillage/Corn___Northern_Leaf_Blight/`

### Step 2️⃣ - Prepare Images (Optional but Recommended)

```bash
# Resize all images to 224×224px, convert to RGB, remove corrupted
python prepare_images.py

# Or just validate dataset structure
python prepare_images.py --validate_only
```

### Step 3️⃣ - Train the Model

```bash
# Quick train (20 epochs, good for starting)
python train_model.py --epochs 20

# Advanced train (50 epochs, better accuracy)
python train_model.py --epochs 50

# With image preparation
python train_model.py --epochs 20 --prepare_images
```

### Step 4️⃣ - Test Updated Model

```bash
# Start Flask app
python app.py

# Then upload:
# - Apple leaf → should show "Apple___Black_rot" 
# - Corn leaf → should show "Corn___Northern_Leaf_Blight"
# - etc.

# Disease info and remedies should display correctly ✅
```

---

## Expected Training Output

```
================================================================
🌾 CROP DISEASE MODEL TRAINING
================================================================

📂 Dataset: D:\crop_disease_project\PlantVillage
📊 Classes found: 34
🔧 Configuration:
   - Epochs: 20
   - Batch size: 32
   - Image size: 224×224px

🎯 Starting training...

✓ Found 34 disease classes:
  1. Pepper__bell___Bacterial_spot
  2. Pepper__bell___healthy
  ...
  34. Cucumber___healthy

Loading dataset...
Epoch 1/20 - Loss: 3.45 - Acc: 12% - Val Loss: 2.89 - Val Acc: 28%
Epoch 2/20 - Loss: 2.34 - Acc: 45% - Val Loss: 1.89 - Val Acc: 52%
...
Epoch 20/20 - Loss: 0.23 - Acc: 94% - Val Loss: 0.45 - Val Acc: 89%

✅ TRAINING COMPLETE!
================================================================
```

---

## 🎯 What You Get After Training

✅ **model.h5** - Trained neural network (223 MB)
✅ **saved_model/** - TensorFlow SavedModel format
✅ **Predictions** - Can now detect 34 disease types
✅ **Disease Info** - Shows crop, disease name, and treatment solution

Example output when uploading apple leaf image:
```
🍎 Crop: Apple
🦠 Disease: Black Rot
💊 Solution: Prune out infected branches, remove cankers, 
   apply copper fungicide, and maintain good orchard sanitation.
```

---

## 📚 Detailed Documentation

See **TRAINING_GUIDE.md** for:
- Complete folder structure
- Detailed image download instructions
- Troubleshooting
- FAQ

---

## ⚡ Minimum Quick Start (If you're in a hurry)

Just retrain with existing 3 crops:

```bash
# 1. Make sure you have existing images in PlantVillage/
# 2. Train
python train_model.py --epochs 10

# 3. Test
python app.py
```

Done! ✅

---

## 🐛 If Images Still Show Wrong Crop Names

1. Check model was retrained: `ls -la model.h5` (should be recent)
2. Restart Flask: Press Ctrl+C and run `python app.py`
3. Clear browser cache: Ctrl+Shift+Delete
4. Check disease_info.py has entries for your crop
5. Validate with: `python prepare_images.py --validate_only`

---

**Questions?** See TRAINING_GUIDE.md or create an issue! 🌾
