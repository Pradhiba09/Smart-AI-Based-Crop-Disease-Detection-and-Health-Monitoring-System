# EXACT STEP-BY-STEP TRAINING GUIDE
## Complete Project Training Instructions

---

## **STEP 1: DOWNLOAD THE DATASET** 
**(On your computer, using browser)**

1. Open your web browser (Chrome, Firefox, Edge)
2. Go to: **https://www.kaggle.com/datasets/arjuntejaswi/plant-village**
3. Click the blue **"Download"** button
4. Wait for the file to download (~2-3 GB, takes 15-30 minutes)
5. You'll get a file named: **archive.zip** or **plant-village.zip**

✅ **Result:** You have a ZIP file with all crop disease images

---

## **STEP 2: EXTRACT THE DATASET**
**(On your computer, using File Explorer)**

1. Open **File Explorer** (Windows key + E)
2. Go to: **C:\Users\PRADHIBA S\Downloads** (where your ZIP file is)
3. **Right-click** on the ZIP file → **"Extract All"**
4. When asked where to extract, click **"Browse"**
5. Select: **C:\Users\PRADHIBA S\Downloads** (or any folder you want)
6. Click **"Extract"** and wait (2-5 minutes)

✅ **Result:** You now have a folder like: **C:\Users\PRADHIBA S\Downloads\archive**

**The folder structure should look like:**
```
C:\Users\PRADHIBA S\Downloads\archive\
├── Apple___Apple_scab/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── Apple___Black_rot/
├── Tomato___Early_blight/
├── Tomato___Late_blight/
├── Potato___Early_blight/
└── ... (many more folders)
```

---

## **STEP 3: OPEN POWERSHELL TERMINAL**
**(On your computer)**

1. Press **Windows Key + R**
2. Type: **powershell**
3. Press **Enter**

✅ **Result:** A terminal window opens (white/blue text on black background)

---

## **STEP 4: NAVIGATE TO YOUR PROJECT FOLDER**
**(In PowerShell terminal)**

Type this command and press **Enter**:

```powershell
cd "c:\Users\PRADHIBA S\Desktop\crop_disease_project"
```

You should see:
```
PS C:\Users\PRADHIBA S\Desktop\crop_disease_project>
```

✅ **Result:** You're now in your project folder

---

## **STEP 5: ACTIVATE VIRTUAL ENVIRONMENT**
**(In PowerShell terminal)**

Type this command and press **Enter**:

```powershell
venv\Scripts\Activate.ps1
```

You should see the terminal change to:
```
(venv) PS C:\Users\PRADHIBA S\Desktop\crop_disease_project>
```

**Notice:** There's now **(venv)** at the beginning. This means the virtual environment is active.

✅ **Result:** Virtual environment is activated

---

## **STEP 6: START TRAINING**
**(In PowerShell terminal - with (venv) active)**

Type this command and press **Enter**:

```powershell
python train_real_model.py --dataset_path "C:\Users\PRADHIBA S\Downloads\archive" --epochs 20
```

**IMPORTANT:** Replace the path with YOUR actual dataset path:
- If you extracted to Downloads: `"C:\Users\PRADHIBA S\Downloads\archive"`
- If you extracted somewhere else, use that path instead

The terminal will show:
```
✓ Found 38 disease classes
Loading dataset...
📊 Dataset loaded successfully!
   Training samples: 15000
   Validation samples: 3750
Building model...
🧠 Training model for 20 epochs...
Epoch 1/20
200/200 [=========================>] - 120s - loss: 1.45 - accuracy: 0.65
Epoch 2/20
...
```

⏱️ **This will take 20-45 minutes depending on your computer!**

**DO NOT CLOSE THE TERMINAL during training!**

✅ **Result:** After training completes, you'll see:
```
✓ Validation Accuracy: 92.45%
✓ Model saved to 'saved_model/' directory
✓ Class mapping saved to 'class_mapping.json'
```

---

## **STEP 7: WAIT FOR TRAINING TO FINISH**
**(In PowerShell terminal - DO NOT TOUCH)**

- You'll see progress bars for each epoch
- Each epoch takes 1-3 minutes
- Total time: ~20-45 minutes
- **DO NOT:**
  - Close the terminal
  - Stop the process
  - Close your computer
  - Restart

✅ **Result:** Training completes and shows final accuracy

---

## **STEP 8: START THE WEB APP**
**(In PowerShell terminal - same one)**

Once training finishes, type this and press **Enter**:

```powershell
python app.py
```

You should see:
```
✓ Loaded model from SavedModel directory
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

✅ **Result:** Flask web app is now running

---

## **STEP 9: TEST YOUR APP**
**(On your computer, using browser)**

1. Open your web browser (Chrome, Firefox, etc.)
2. Go to: **http://127.0.0.1:5000**
3. You should see the green page with:
   - Title: "🌱 Crop Disease Detection System"
   - A button to upload images
4. Click **"Choose File"**
5. Select any image (can be a crop leaf photo, or any image)
6. Click **"Predict"**
7. The app will show the disease prediction!

✅ **Result:** Your trained model works and predicts diseases!

---

## **STEP 10: TAKE SCREENSHOTS FOR YOUR PROJECT**
**(On your computer)**

1. Take screenshots showing:
   - The web app upload interface
   - Prediction results
   - Accuracy metrics from training output
2. Save them for your final year project report

✅ **Result:** You have proof the app works

---

## **FINAL: STOP THE APP**
**(In PowerShell terminal)**

When done testing:
1. Go back to the PowerShell terminal
2. Press **CTRL + C**
3. The app stops and you get the prompt back

```
(venv) PS C:\Users\PRADHIBA S\Desktop\crop_disease_project>
```

---

# 📋 QUICK REFERENCE COMMANDS

Copy-paste these into PowerShell:

**1. Navigate to project:**
```powershell
cd "c:\Users\PRADHIBA S\Desktop\crop_disease_project"
```

**2. Activate environment:**
```powershell
venv\Scripts\Activate.ps1
```

**3. Train model (MOST IMPORTANT):**
```powershell
python train_real_model.py --dataset_path "C:\Users\PRADHIBA S\Downloads\archive" --epochs 20
```

**4. Run web app:**
```powershell
python app.py
```

**5. Stop app:**
```
Press CTRL + C
```

---

# ❓ TROUBLESHOOTING

### **Problem: "No class folders found"**
- ✅ Check dataset path is correct
- ✅ Make sure you extracted the ZIP file
- ✅ Look for folders like "Apple___Apple_scab"

### **Problem: "Out of memory" or "Out of GPU memory"**
- ✅ Use smaller batch size:
```powershell
python train_real_model.py --dataset_path "C:\Users\PRADHIBA S\Downloads\archive" --epochs 20 --batch_size 16
```
- ✅ Or reduce epochs: `--epochs 10`

### **Problem: Training is very slow**
- ✅ This is NORMAL! Can take 30-60 minutes
- ✅ Don't close terminal
- ✅ Faster computers train faster

### **Problem: Web app won't start**
- ✅ Make sure venv is activated (should see `(venv)` in terminal)
- ✅ Check `saved_model/` folder exists
- ✅ Try: `python app.py` again

### **Problem: Browser says "Cannot reach"**
- ✅ Make sure PowerShell shows "Running on http://127.0.0.1:5000"
- ✅ Try different port: modify app.py last line to `app.run(port=5001)`

---

# 📝 FOR YOUR FINAL YEAR PROJECT REPORT

Write something like:

> "The model was trained on the PlantVillage dataset containing 38 disease classes across 14 crop types. Using a Convolutional Neural Network with 4 convolutional layers and dropout regularization, the model achieved [INSERT YOUR ACCURACY]% validation accuracy after [INSERT YOUR TIME] minutes of training on [INSERT YOUR SETUP: CPU/GPU]. The trained model was integrated into a Flask web application allowing real-time crop disease detection."

**Document:**
- ✅ Training time taken
- ✅ Final accuracy percentage
- ✅ Number of epochs used
- ✅ Batch size used
- ✅ Number of images used
- ✅ Diseases detected

---

# ✨ SUMMARY

| Step | What To Do | Time |
|------|-----------|------|
| 1 | Download dataset | 15-30 min |
| 2 | Extract ZIP | 2-5 min |
| 3-4 | Open PowerShell & navigate | 1 min |
| 5 | Activate venv | 30 sec |
| 6-7 | Run training | 20-45 min |
| 8 | Start web app | 5 sec |
| 9 | Test app in browser | 2 min |
| **TOTAL** | **Complete project** | **~1-2 hours** |

---

**You're all set! Follow these steps exactly and your project will be complete! Good luck!** 🎉🌿
