# 🌾 Model Retraining Guide - Updated with 8 Crops

Your project now supports **8 crops with 34 disease classes total**:

## Crops Configuration
| Crop | Classes | Status |
|------|---------|--------|
| 🌶️ Pepper Bell | 2 | ✅ Existing |
| 🥔 Potato | 3 | ✅ Existing |
| 🍅 Tomato | 7 | ✅ Existing |
| 🍎 Apple | 4 | ⏳ New |
| 🌽 Corn | 4 | ⏳ New |
| 🍇 Grape | 4 | ⏳ New |
| 🌾 Wheat | 4 | ⏳ New |
| 🥒 Cucumber | 3 | ⏳ New |

---

## Step 1: Prepare Your Images

### For NEW crops (Apple, Corn, Grape, Wheat, Cucumber):

Get images from any of these sources:
- **Google Images** - Download 50-100 images per disease
- **Kaggle Datasets** - Search specific crop diseases
- **iNaturalist** - Download with proper licenses
- **Your own photos** - Take pictures of diseased crops

### Folder Structure Required:
```
PlantVillage/
├── Pepper__bell___Bacterial_spot/     (existing - keep as is)
├── Pepper__bell___healthy/            (existing - keep as is)
├── Potato___Early_blight/             (existing - keep as is)
├── Potato___Late_blight/              (existing - keep as is)
├── Potato___healthy/                  (existing - keep as is)
├── Tomato_Bacterial_spot/             (existing - keep as is)
├── Tomato_Early_blight/               (existing - keep as is)
├── Tomato_Late_blight/                (existing - keep as is)
├── Tomato_Leaf_Mold/                  (existing - keep as is)
├── Tomato_Septoria_leaf_spot/         (existing - keep as is)
├── Tomato_Spider_mites_Two_spotted_spider_mite/  (existing - keep as is)
├── Tomato__Target_Spot/               (existing - keep as is)
├── Tomato__Tomato_YellowLeaf__Curl_Virus/  (existing - keep as is)
├── Tomato__Tomato_mosaic_virus/       (existing - keep as is)
├── Tomato_healthy/                    (existing - keep as is)
│
├── Apple___Apple_scab/                (NEW - add 50+ images)
├── Apple___Black_rot/                 (NEW - add 50+ images)
├── Apple___Cedar_apple_rust/          (NEW - add 50+ images)
├── Apple___healthy/                   (NEW - add 50+ images)
│
├── Corn___Cercospora_leaf_spot/       (NEW - add 50+ images)
├── Corn___Common_rust/                (NEW - add 50+ images)
├── Corn___Northern_Leaf_Blight/       (NEW - add 50+ images)
├── Corn___healthy/                    (NEW - add 50+ images)
│
├── Grape___Black_rot/                 (NEW - add 50+ images)
├── Grape___Esca/                      (NEW - add 50+ images)
├── Grape___Leaf_blight/               (NEW - add 50+ images)
├── Grape___healthy/                   (NEW - add 50+ images)
│
├── Wheat___Leaf_rust/                 (NEW - add 50+ images)
├── Wheat___Stripe_rust/               (NEW - add 50+ images)
├── Wheat___Tan_spot/                  (NEW - add 50+ images)
├── Wheat___healthy/                   (NEW - add 50+ images)
│
├── Cucumber___Angular_leaf_spot/      (NEW - add 50+ images)
├── Cucumber___Downy_mildew/           (NEW - add 50+ images)
└── Cucumber___healthy/                (NEW - add 50+ images)
```

**Required:** Each folder should have **at least 50-100 images** (more is better!).

---

## Step 2: Image Preparation (Optional but Recommended)

Run this to resize all images to 224×224px:

```bash
python prepare_images.py
```

This will:
- Resize all images to 224px × 224px
- Convert to RGB format
- Remove corrupted images
- Save optimized versions

---

## Step 3: Retrain the Model

### Option A: Quick Start (Recommended with 20 epochs)
```bash
python train_real_model.py --dataset_path PlantVillage --epochs 20
```

### Option B: Advanced Training
```bash
python train_real_model.py --dataset_path PlantVillage --epochs 50 --batch_size 32
```

**Training Parameters:**
- `--epochs`: Number of training iterations (default: 20)
- `--batch_size`: Images processed per iteration (default: 32)
- `--dataset_path`: Path to PlantVillage folder (required)

---

## Step 4: What to Expect

### During Training:
```
✓ Found 34 disease classes:
  1. Pepper__bell___Bacterial_spot
  2. Pepper__bell___healthy
  ...
  34. Cucumber___healthy

Loading dataset...
Training: Epoch 1/20
  Batch 50/200 | Loss: 2.34 | Acc: 45%
  ...
  
Validating: Loss: 1.89 | Acc: 52%

✓ Model trained! Saved to model.h5 and saved_model/
```

### Training Time:
- **With GPU**: 10-30 minutes for 20 epochs
- **With CPU**: 1-3 hours for 20 epochs

---

## Step 5: Test Your Updated Model

1. **Restart Flask App:**
   ```bash
   python app.py
   ```

2. **Upload Image:**
   - Upload an apple leaf image
   - Model should show: `Apple___Black_rot` with remedies
   - Disease info should display correctly

3. **Check Disease Info:**
   The app should now display:
   - ✅ Crop name (Apple, Corn, Grape, Wheat, Cucumber)
   - ✅ Disease name
   - ✅ Treatment solution

---

## Troubleshooting

### ❌ "Model output size doesn't match CLASS_NAMES"
**Solution:** Your model has 15 outputs but expects 34. You must retrain!

### ❌ "No images found in dataset"
**Solution:** Check folder structure - images must be in `PlantVillage/ClassName/image.jpg`

### ❌ "Folder exists but empty"
**Solution:** Make sure you're copying images to the correct folders

### ❌ Predictions Still Show Wrong Crop Names
**Solution:** 
1. Make sure you retrained the model
2. Restart Flask: Press `Ctrl+C` and run `python app.py` again
3. Browser cache: Press `Ctrl+Shift+Delete` to clear cache

---

## Disease Info Reference

All disease solutions are pre-configured. When model predicts a disease:

**Example - Apple Scab:**
```
Crop: Apple
Disease: Apple Scab
Solution: Remove infected leaves and fallen fruit, apply fungicide 
(sulfur or mancozeb), improve air circulation, and use resistant varieties.
```

---

## FAQ

**Q: Can I retrain without all 8 crops?**
A: Yes! You can train with just 3-5 crops. Just leave empty folders (they'll be skipped) or remove them.

**Q: How many images do I need per class?**
A: Minimum 30-50, but 100+ per class gives much better accuracy.

**Q: Can I add more crops later?**
A: Yes! Update `disease_info.py` and `class_mapping.json`, then retrain the model.

**Q: Will retraining delete my old model?**
A: Yes, it saves to `model.h5` and `saved_model/`. Backup first if needed.

---

## Next Steps

1. ✅ Created folder structure (Done!)
2. ⏳ Download/prepare images for new crops
3. ⏳ Run training script
4. ⏳ Test the new model
5. ⏳ Deploy to production

Good luck! 🚀
