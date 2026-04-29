"""
Comprehensive crop disease information database.
Includes all diseases from PlantVillage dataset.
"""

DISEASE_INFO = {
    # APPLE DISEASES
    "Apple___Apple_scab": {
        "crop": "Apple",
        "disease": "Apple Scab",
        "solution": "Prune infected branches. Remove fallen leaves. Apply fungicide (sulfur or copper) every 7-14 days."
    },
    "Apple___Black_rot": {
        "crop": "Apple",
        "disease": "Black Rot",
        "solution": "Remove infected fruit and branches. Apply fungicide. Improve air circulation around tree."
    },
    "Apple___Cedar_apple_rust": {
        "crop": "Apple",
        "disease": "Cedar Apple Rust",
        "solution": "Remove galls from nearby cedar/juniper trees. Apply fungicide (sulfur) during growing season."
    },
    "Apple___healthy": {
        "crop": "Apple",
        "disease": "Healthy",
        "solution": "Plant is healthy! Maintain regular watering, pruning, and monitoring."
    },
    
    # TOMATO DISEASES
    "Tomato___Bacterial_spot": {
        "crop": "Tomato",
        "disease": "Bacterial Spot",
        "solution": "Remove infected leaves. Use copper sulfate or chlorothalonil spray. Avoid overhead watering."
    },
    "Tomato___Early_blight": {
        "crop": "Tomato",
        "disease": "Early Blight",
        "solution": "Remove lower infected leaves. Apply mancozeb or chlorothalonil weekly. Improve air circulation."
    },
    "Tomato___Late_blight": {
        "crop": "Tomato",
        "disease": "Late Blight",
        "solution": "Remove infected parts. Apply mancozeb, chlorothalonil, or metalaxyl. Water at soil level only."
    },
    "Tomato___Leaf_Mold": {
        "crop": "Tomato",
        "disease": "Leaf Mold",
        "solution": "Increase ventilation. Remove infected leaves. Apply sulfur or triadimefon spray."
    },
    "Tomato___Septoria_leaf_spot": {
        "crop": "Tomato",
        "disease": "Septoria Leaf Spot",
        "solution": "Remove infected leaves. Apply chlorothalonil or mancozeb. Maintain proper spacing for airflow."
    },
    "Tomato___Spider_mites": {
        "crop": "Tomato",
        "disease": "Spider Mites",
        "solution": "Spray with neem oil or sulfur. Increase humidity. Remove heavily infested leaves. Use miticides if severe."
    },
    "Tomato___Target_Spot": {
        "crop": "Tomato",
        "disease": "Target Spot",
        "solution": "Remove infected leaves. Apply chlorothalonil or mancozeb. Improve greenhouse ventilation."
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "crop": "Tomato",
        "disease": "Yellow Leaf Curl Virus",
        "solution": "Remove infected plants immediately. Control whiteflies with insecticide. Use resistant varieties."
    },
    "Tomato___Tomato_mosaic_virus": {
        "crop": "Tomato",
        "disease": "Tomato Mosaic Virus",
        "solution": "Remove and destroy infected plants. Sterilize tools. Use resistant varieties. Control aphids with spray."
    },
    "Tomato___healthy": {
        "crop": "Tomato",
        "disease": "Healthy",
        "solution": "Plant is healthy! Continue regular watering, pruning, and nutrient management."
    },
    
    # POTATO DISEASES
    "Potato___Early_blight": {
        "crop": "Potato",
        "disease": "Early Blight",
        "solution": "Remove infected leaves. Apply chlorothalonil or mancozeb. Use crop rotation (3-4 year interval)."
    },
    "Potato___Late_blight": {
        "crop": "Potato",
        "disease": "Late Blight",
        "solution": "Remove infected plants immediately. Apply metalaxyl or mancozeb spray. Improve drainage and airflow."
    },
    "Potato___healthy": {
        "crop": "Potato",
        "disease": "Healthy",
        "solution": "Potato plant is healthy! Maintain proper irrigation and monitor for pests regularly."
    },
    
    # CORN/MAIZE DISEASES
    "Corn (maize)___Cercospora_leaf_spot": {
        "crop": "Corn",
        "disease": "Cercospora Leaf Spot",
        "solution": "Use resistant varieties. Remove crop residue after harvest. Apply fungicide if severe."
    },
    "Corn (maize)___Common_rust": {
        "crop": "Corn",
        "disease": "Common Rust",
        "solution": "Plant resistant varieties. Remove infected leaves if possible. Apply fungicide in severe cases."
    },
    "Corn (maize)___Northern_Leaf_Blight": {
        "crop": "Corn",
        "disease": "Northern Leaf Blight",
        "solution": "Use resistant hybrids. Remove crop residue. Apply fungicide during growing season."
    },
    "Corn (maize)___healthy": {
        "crop": "Corn",
        "disease": "Healthy",
        "solution": "Corn plant is healthy! Monitor soil moisture and nutrient levels regularly."
    },
    
    # GRAPE DISEASES
    "Grape___Black_rot": {
        "crop": "Grape",
        "disease": "Black Rot",
        "solution": "Remove infected berries and shoots. Apply sulfur or copper spray. Improve air circulation."
    },
    "Grape___Esca": {
        "crop": "Grape",
        "disease": "Esca (Grapevine Trunk Disease)",
        "solution": "Remove infected canes. Prune carefully to minimize wounds. No effective cure; prevention is key."
    },
    "Grape___Leaf_blight": {
        "crop": "Grape",
        "disease": "Leaf Blight",
        "solution": "Remove infected leaves. Apply copper fungicide. Prune to improve air circulation."
    },
    "Grape___healthy": {
        "crop": "Grape",
        "disease": "Healthy",
        "solution": "Grapevine is healthy! Continue regular pruning and monitoring."
    },
    
    # SQUASH DISEASES
    "Squash___Powdery_mildew": {
        "crop": "Squash",
        "disease": "Powdery Mildew",
        "solution": "Spray with sulfur or neem oil weekly. Improve air circulation. Remove heavily infected leaves."
    },
    
    # STRAWBERRY DISEASES
    "Strawberry___Leaf_scorch": {
        "crop": "Strawberry",
        "disease": "Leaf Scorch",
        "solution": "Remove infected leaves. Apply fungicide. Avoid overhead watering. Improve air circulation."
    },
    "Strawberry___healthy": {
        "crop": "Strawberry",
        "disease": "Healthy",
        "solution": "Strawberry plant is healthy! Maintain proper spacing and water management."
    },
    
    # PEPPER DISEASES
    "Pepper___Bacterial_spot": {
        "crop": "Pepper",
        "disease": "Bacterial Spot",
        "solution": "Remove infected leaves. Apply copper sulfate spray. Avoid overhead watering."
    },
    "Pepper___healthy": {
        "crop": "Pepper",
        "disease": "Healthy",
        "solution": "Pepper plant is healthy! Continue regular watering and avoid over-fertilizing."
    },
}


def get_disease_info(class_name):
    """
    Get disease information by class name.
    
    Args:
        class_name: Disease class name (e.g., "Tomato___Early_blight")
    
    Returns:
        Dictionary with crop, disease, and solution information.
    """
    if class_name in DISEASE_INFO:
        return DISEASE_INFO[class_name]
    else:
        return {
            "crop": "Unknown",
            "disease": class_name.replace("___", " - ").replace("_", " "),
            "solution": "Disease not in database. Please check the classification."
        }


if __name__ == "__main__":
    # Print all available diseases
    print("Available Crops and Diseases:\n")
    crops = {}
    for class_name, info in DISEASE_INFO.items():
        crop = info["crop"]
        if crop not in crops:
            crops[crop] = []
        crops[crop].append(info["disease"])
    
    for crop in sorted(crops.keys()):
        print(f"\n{crop}:")
        for disease in sorted(set(crops[crop])):
            print(f"  - {disease}")
