#!/usr/bin/env python
"""
Image Preparation Script for Crop Disease Detection
Resizes, converts, and validates images in PlantVillage dataset
"""

import os
import argparse
from pathlib import Path
from PIL import Image
import traceback

def prepare_images(dataset_path="PlantVillage", target_size=224, delete_corrupted=False):
    """
    Prepare all images in dataset:
    - Resize to target size × target size
    - Convert to RGB
    - Remove corrupted/invalid images
    """
    
    dataset_path = Path(dataset_path)
    
    if not dataset_path.exists():
        print(f"❌ Error: Dataset path not found: {dataset_path}")
        return False
    
    classes = [d for d in dataset_path.iterdir() if d.is_dir()]
    
    if not classes:
        print(f"❌ No class folders found in {dataset_path}")
        return False
    
    print(f"\n🌾 Preparing images for {len(classes)} classes...")
    print(f"Target size: {target_size}×{target_size}px\n")
    
    total_processed = 0
    total_corrupted = 0
    
    for class_dir in sorted(classes):
        class_name = class_dir.name
        images = list(class_dir.glob("*.jpg")) + list(class_dir.glob("*.JPG")) + \
                 list(class_dir.glob("*.png")) + list(class_dir.glob("*.PNG")) + \
                 list(class_dir.glob("*.jpeg")) + list(class_dir.glob("*.JPEG"))
        
        if not images:
            print(f"⚠️  {class_name}: No images found")
            continue
        
        print(f"📂 Processing {class_name}... ({len(images)} images)", end=" ")
        
        processed = 0
        corrupted = 0
        
        for img_path in images:
            try:
                # Open image
                img = Image.open(img_path)
                
                # Convert RGBA or grayscale to RGB
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Resize
                img = img.resize((target_size, target_size), Image.Resampling.LANCZOS)
                
                # Save back (overwrites original)
                img.save(img_path, quality=95)
                processed += 1
                
            except Exception as e:
                corrupted += 1
                total_corrupted += 1
                
                if delete_corrupted:
                    try:
                        img_path.unlink()
                        print(f"\n   Deleted corrupt: {img_path.name}")
                    except:
                        pass
                else:
                    print(f"\n   ⚠️  Corrupt: {img_path.name}")
        
        total_processed += processed
        print(f"✅ {processed} OK", end="")
        if corrupted > 0:
            print(f" | ⚠️  {corrupted} corrupted", end="")
        print()
    
    print(f"\n{'='*60}")
    print(f"✅ Total processed: {total_processed} images")
    if total_corrupted > 0:
        print(f"⚠️  Total corrupted: {total_corrupted} images")
    print(f"{'='*60}\n")
    
    return True

def validate_dataset(dataset_path="PlantVillage"):
    """Check if dataset has minimum images per class"""
    
    dataset_path = Path(dataset_path)
    
    if not dataset_path.exists():
        print(f"❌ Dataset path not found: {dataset_path}")
        return False
    
    print(f"\n📊 Dataset Validation Report")
    print(f"{'='*60}")
    
    classes_info = {}
    total_images = 0
    min_images = float('inf')
    max_images = 0
    short_classes = []
    
    for class_dir in sorted(dataset_path.iterdir()):
        if not class_dir.is_dir():
            continue
        
        images = list(class_dir.glob("*.[jJ][pP][gG]")) + \
                 list(class_dir.glob("*.[pP][nN][gG]")) + \
                 list(class_dir.glob("*.[jJ][pP][eE][gG]"))
        
        count = len(images)
        classes_info[class_dir.name] = count
        total_images += count
        min_images = min(min_images, count)
        max_images = max(max_images, count)
        
        status = "✅" if count >= 50 else "⚠️ " if count >= 30 else "❌"
        print(f"{status} {class_dir.name}: {count} images")
        
        if count < 50:
            short_classes.append((class_dir.name, count))
    
    print(f"\n{'='*60}")
    print(f"Total classes: {len(classes_info)}")
    print(f"Total images: {total_images}")
    print(f"Average per class: {total_images // len(classes_info) if classes_info else 0}")
    print(f"Min per class: {min_images if min_images != float('inf') else 0}")
    print(f"Max per class: {max_images}")
    print(f"{'='*60}\n")
    
    if short_classes:
        print("⚠️  Classes with < 50 images (consider adding more):")
        for cls, count in short_classes:
            print(f"   • {cls}: {count} images")
        print()
    
    if total_images < len(classes_info) * 50:
        print("📌 Recommendation: Add more images for better accuracy")
        missing = (len(classes_info) * 50) - total_images
        print(f"   → Add ~{missing} more images across classes\n")
    else:
        print("✅ Dataset looks good! Ready for training.\n")
    
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Prepare crop disease images for training"
    )
    parser.add_argument(
        "--dataset_path",
        default="PlantVillage",
        help="Path to PlantVillage dataset (default: PlantVillage)"
    )
    parser.add_argument(
        "--size",
        type=int,
        default=224,
        help="Target image size in pixels (default: 224)"
    )
    parser.add_argument(
        "--delete_corrupted",
        action="store_true",
        help="Delete corrupted images (default: keep and warn)"
    )
    parser.add_argument(
        "--validate_only",
        action="store_true",
        help="Only validate dataset without processing"
    )
    
    args = parser.parse_args()
    
    if args.validate_only:
        validate_dataset(args.dataset_path)
    else:
        prepare_images(args.dataset_path, args.size, args.delete_corrupted)
        validate_dataset(args.dataset_path)
