#!/usr/bin/env python
"""
Automatic Image Downloader for Crop Disease Dataset
Downloads images from Bing Image Search for each disease class
"""

import os
import argparse
from pathlib import Path
import time

def install_bing_downloader():
    """Install bing-image-downloader if not present"""
    try:
        import bing_image_downloader
        return True
    except ImportError:
        print("Installing bing-image-downloader...")
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "bing-image-downloader"])
        return True

def download_images(disease_class, num_images=100, output_dir="PlantVillage"):
    """Download images for a specific disease class"""
    try:
        from bing_image_downloader import downloader
    except ImportError:
        print("❌ bing-image-downloader not installed. Run with --install flag first.")
        return False
    
    # Create search query from class name
    # Example: "Apple___Apple_scab" → "apple scab disease"
    parts = disease_class.replace("___", "_").replace("__", "_").split("_")
    
    # Remove words like "healthy"
    if parts[-1].lower() == "healthy":
        search_query = f"{parts[0].lower()} healthy leaf"
    else:
        # Join remaining parts with spaces
        search_query = " ".join(parts).lower()
        search_query += " disease leaf"
    
    output_path = os.path.join(output_dir, disease_class)
    os.makedirs(output_path, exist_ok=True)
    
    print(f"📥 Downloading {disease_class}...")
    print(f"   Search: '{search_query}'")
    print(f"   Target: {num_images} images")
    
    try:
        downloader.download(
            query=search_query,
            limit=num_images,
            output_dir="dataset",
            adult_filter_off=True,
            force_replace=False,
            timeout=60
        )
        
        # Move images from temporary folder to target folder
        dataset_path = Path("dataset") / search_query
        if dataset_path.exists():
            for img_file in dataset_path.glob("*.*"):
                if img_file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
                    img_file.rename(Path(output_path) / img_file.name)
            
            # Clean up temp folder
            try:
                dataset_path.rmdir()
            except:
                pass
        
        # Count downloaded images
        downloaded = len(list(Path(output_path).glob("*.*")))
        print(f"   ✅ Downloaded {downloaded} images\n")
        return True
        
    except Exception as e:
        print(f"   ⚠️  Error: {e}\n")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="Download crop disease images for training"
    )
    parser.add_argument(
        "--disease",
        help="Download specific disease class (e.g., Apple___Apple_scab)"
    )
    parser.add_argument(
        "--crop",
        help="Download all diseases for a crop (e.g., Apple)"
    )
    parser.add_argument(
        "--num_images",
        type=int,
        default=50,
        help="Number of images per class (default: 50)"
    )
    parser.add_argument(
        "--install",
        action="store_true",
        help="Install bing-image-downloader dependency"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Download for all new crops (Apple, Corn, Grape, Wheat, Cucumber)"
    )
    
    args = parser.parse_args()
    
    # Install if requested
    if args.install:
        print("📦 Installing bing-image-downloader...")
        if install_bing_downloader():
            print("✅ Installation complete!\n")
        else:
            print("❌ Installation failed\n")
            return False
    
    # Define crop diseases
    crops_diseases = {
        "Apple": [
            "Apple___Apple_scab",
            "Apple___Black_rot",
            "Apple___Cedar_apple_rust",
            "Apple___healthy"
        ],
        "Corn": [
            "Corn___Cercospora_leaf_spot",
            "Corn___Common_rust",
            "Corn___Northern_Leaf_Blight",
            "Corn___healthy"
        ],
        "Grape": [
            "Grape___Black_rot",
            "Grape___Esca",
            "Grape___Leaf_blight",
            "Grape___healthy"
        ],
        "Wheat": [
            "Wheat___Leaf_rust",
            "Wheat___Stripe_rust",
            "Wheat___Tan_spot",
            "Wheat___healthy"
        ],
        "Cucumber": [
            "Cucumber___Angular_leaf_spot",
            "Cucumber___Downy_mildew",
            "Cucumber___healthy"
        ]
    }
    
    # Determine what to download
    classes_to_download = []
    
    if args.disease:
        classes_to_download = [args.disease]
    elif args.crop:
        if args.crop in crops_diseases:
            classes_to_download = crops_diseases[args.crop]
        else:
            print(f"❌ Crop '{args.crop}' not found. Available: {', '.join(crops_diseases.keys())}")
            return False
    elif args.all:
        for crop_classes in crops_diseases.values():
            classes_to_download.extend(crop_classes)
    else:
        print("Please specify: --disease, --crop, or --all")
        parser.print_help()
        return False
    
    if not classes_to_download:
        print("No classes to download")
        return False
    
    # Check if bing-image-downloader is available
    try:
        from bing_image_downloader import downloader
    except ImportError:
        print("❌ bing-image-downloader not installed")
        print("\nInstall with: python download_images.py --install")
        print("Then run: python download_images.py --all --num_images 50")
        return False
    
    print("="*70)
    print(f"📥 DOWNLOADING IMAGES FOR {len(classes_to_download)} CLASSES")
    print("="*70 + "\n")
    
    successful = 0
    failed = 0
    
    for i, disease_class in enumerate(classes_to_download, 1):
        print(f"[{i}/{len(classes_to_download)}]", end=" ")
        
        if download_images(disease_class, args.num_images):
            successful += 1
        else:
            failed += 1
        
        # Small delay between downloads to avoid rate limiting
        if i < len(classes_to_download):
            time.sleep(2)
    
    print("="*70)
    print(f"✅ Downloaded: {successful} classes")
    if failed > 0:
        print(f"⚠️  Failed: {failed} classes")
    print("="*70 + "\n")
    
    print("📊 Summary:")
    print(f"   Total images: ~{successful * args.num_images}")
    print(f"   Location: PlantVillage/")
    print(f"\n✅ Ready to train model! Run: python train_model.py --epochs 20\n")
    
    return True

if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)
