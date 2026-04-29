# How to Use PlantVillage Dataset with Your Crop Disease Detection App

## Step 1: Download PlantVillage Dataset

You have **2 options:**

### Option A: Download from Kaggle (Easiest)
1. Go to: https://www.kaggle.com/datasets/arjuntejaswi/plant-village
2. Click "Download" (requires Kaggle account)
3. Extract the downloaded ZIP file

### Option B: Download from GitHub
1. Go to: https://github.com/spMohanty/PlantVillage-Dataset
2. Clone or download as ZIP
3. Extract the files

---

## Step 2: Prepare Dataset Structure

After extraction, your dataset should look like:
```
PlantVillage/
  ├── Apple___Apple_scab/
  │   ├── image1.jpg
  │   ├── image2.jpg
  │   └── ...
  ├── Apple___Black_rot/
  ├── Apple___Cedar_apple_rust/
  ├── Tomato___Bacterial_spot/
  ├── Tomato___Early_blight/
  ├── Tomato___Late_blight/
  ├── Tomato___Leaf_Mold/
  ├── Tomato___Septoria_leaf_spot/
  ├── Tomato___Spider_mites/
  ├── Tomato___Target_Spot/
  ├── Tomato___Tomato_Yellow_Leaf_Curl_Virus/
  ├── Tomato___Tomato_mosaic_virus/
  ├── Tomato___healthy/
  ├── Potato___Early_blight/
  ├── Potato___Late_blight/
  ├── Potato___healthy/
  ├── Corn (maize)___Cercospora_leaf_spot/
  ├── Corn (maize)___Common_rust/
  ├── Corn (maize)___Northern_Leaf_Blight/
  ├── Corn (maize)___healthy/
  ├── Grape___Black_rot/
  ├── Grape___Esca/
  ├── Grape___Leaf_blight/
  ├── Grape___healthy/
  ├── Squash___Powdery_mildew/
  ├── Strawberry___Leaf_scorch/
  ├── Strawberry___healthy/
  ├── Pepper___Bacterial_spot/
  ├── Pepper___healthy/
  └── ... (more crops)
```

---

## Step 3: Train Your Model

Navigate to your project folder and run:

```powershell
# Activate virtual environment
cd "c:\Users\PRADHIBA S\Desktop\crop_disease_project"
venv\Scripts\Activate.ps1

# Train the model (replace PATH with your actual dataset path)
python train_real_model.py --dataset_path "C:\path\to\PlantVillage" --epochs 30

# Example for Windows:
python train_real_model.py --dataset_path "C:\Users\YourName\Downloads\PlantVillage" --epochs 30
```

---

## Step 4: Wait for Training to Complete

This will take **10-30 minutes** depending on:
- Number of images in dataset
- Your computer's speed
- Number of epochs (higher = more accurate but slower)

You'll see progress like:
```
Epoch 1/30
200/200 [=================] - 120s - loss: 2.1234 - accuracy: 0.6543
...
✓ Validation Accuracy: 92.45%
```

---

## Step 5: Check Results

After training:
- **saved_model/** - Your trained model (automatically created)
- **class_mapping.json** - What diseases were detected

---

## Step 6: Run Your Web App

```powershell
# Make sure venv is activated, then:
python app.py
```

Open: http://127.0.0.1:5000

Now upload crop images and it will detect real diseases! 🌾

---

## Crops in PlantVillage Dataset

| Crop | Diseases | Healthy |
|------|----------|---------|
| Apple | Scab, Black Rot, Cedar Apple Rust | ✓ |
| Tomato | Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Mosaic Virus | ✓ |
| Potato | Early Blight, Late Blight | ✓ |
| Corn/Maize | Cercospora Leaf Spot, Common Rust, Northern Leaf Blight | ✓ |
| Grape | Black Rot, Esca, Leaf Blight | ✓ |
| Squash | Powdery Mildew | ✗ |
| Strawberry | Leaf Scorch | ✓ |
| Pepper | Bacterial Spot | ✓ |

---

## Troubleshooting

**Q: Error "No class folders found"**
- Make sure dataset path is correct
- Check that folder structure has crop disease folders

**Q: Out of memory error**
- Reduce batch_size: `--batch_size 16`
- Reduce epochs: `--epochs 10`

**Q: Very slow training**
- This is normal! 30 min to 2 hours is typical
- Don't close the terminal during training

---

## Tips

1. **Smaller dataset** - Extract only some crops (not all)
2. **Faster training** - Use fewer epochs: `--epochs 10`
3. **Better accuracy** - Use more epochs: `--epochs 50` (takes longer)
4. **Test model** - Upload images after training to test predictions
