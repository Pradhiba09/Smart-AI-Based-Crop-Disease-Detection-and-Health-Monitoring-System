# 🌿 Agri Cure - Smart Crop Disease Detection

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.1.2-white?style=flat&logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/TensorFlow-2.x-orange?style=flat&logo=tensorflow" alt="TensorFlow">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat" alt="License">
</p>

> AI-powered crop disease detection system that identifies plant diseases from leaf images using deep learning and provides actionable treatment recommendations.

---

## 🚀 Features

- **📸 Image Upload** - Drag & drop or click to upload leaf images
- **🧠 AI-Powered Detection** - Deep learning CNN model for accurate disease identification
- **📊 Real-time Results** - Instant disease detection with confidence scores
- **💊 Treatment Plans** - Detailed treatment recommendations for each disease
- **🌾 Multi-Crop Support** - Supports Tomato, Potato, Pepper, Apple, Corn, Grape, Cucumber, Wheat
- **📱 Responsive Design** - Works on desktop and mobile devices

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Backend | Flask (Python) |
| AI/ML | TensorFlow, Keras, CNN |
| Frontend | HTML, CSS, JavaScript |
| Styling | Tailwind CSS |

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Pradhiba09/Smart-AI-Based-Crop-Disease-Detection-and-Health-Monitoring-System.git
cd Smart-AI-Based-Crop-Disease-Detection-and-Health-Monitoring-System
```

### 2. Create Virtual Environment
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 4. Run the Application
```powershell
python app.py
```

### 5. Open in Browser
Navigate to: **http://127.0.0.1:5000**

---

## 📁 Project Structure

```
agri-cure/
├── app.py                    # Main Flask application
├── templates/
│   ├── index.html           # Home page
│   └── how_it_works.html    # How It Works page
├── static/
│   ├── style.css           # Custom styles
│   └── uploads/            # Uploaded images
├── requirements.txt        # Python dependencies
├── class_mapping.json      # Class labels (old crops)
├── class_mapping_crop.json # Class labels (new crops)
├── disease_info.py         # Disease information
└── new_crops_guidelines.py # New crops data
```

---

## 🌱 Supported Crops

| Crop | Diseases Detected |
|------|-------------------|
| 🍅 Tomato | Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Mosaic Virus, Yellow Leaf Curl |
| 🥔 Potato | Early Blight, Late Blight, Healthy |
| 🌶️ Pepper | Bacterial Spot, Healthy |
| 🍎 Apple | Apple Scab, Black Rot, Cedar Apple Rust |
| 🌽 Corn | Cercospora Leaf Spot, Common Rust, Northern Leaf Blight |
| 🍇 Grape | Black Rot, Esca, Leaf Blight |
| 🥒 Cucumber | Angular Leaf Spot, Downy Mildew |
| 🌾 Wheat | Leaf Rust, Stripe Rust, Tan Spot |

---

## 📊 Model Performance

- **Accuracy:** 95%+
- **Disease Classes:** 38+
- **Training Data:** 80,000+ plant images

---

## 🔧 How It Works

1. **📤 Upload** - User uploads a clear photo of their crop leaf
2. **⚙️ Preprocess** - Image is resized to 128x128 and normalized
3. **🧠 AI Analysis** - CNN model analyzes patterns against disease signatures
4. **📊 Results** - Returns disease name, confidence score & treatment plan

---

## 📝 License

This project is licensed under the **MIT License**.

---

## 🙏 Acknowledgments

- [PlantVillage Dataset](https://github.com/spMohanty/PlantVillage-Dataset) - Training data
- [TensorFlow](https://www.tensorflow.org/) - Deep learning framework

---

<p align="center">🌱 Growing healthy crops with AI</p>