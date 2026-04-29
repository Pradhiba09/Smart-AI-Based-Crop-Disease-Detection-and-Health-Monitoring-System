#!/usr/bin/env python
"""
Quick Training Script for Crop Disease Model
Simplified wrapper for train_real_model.py with sensible defaults
"""

import os
import subprocess
import sys
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        description="Train crop disease detection model with new crops"
    )
    parser.add_argument(
        "--epochs",
        type=int,
        default=20,
        help="Number of training epochs (default: 20)"
    )
    parser.add_argument(
        "--batch_size",
        type=int,
        default=32,
        help="Batch size for training (default: 32)"
    )
    parser.add_argument(
        "--prepare_images",
        action="store_true",
        help="Prepare/resize images before training"
    )
    parser.add_argument(
        "--validate_only",
        action="store_true",
        help="Only validate dataset without training"
    )
    
    args = parser.parse_args()
    
    dataset_path = Path("PlantVillage")
    
    # Check if dataset exists
    if not dataset_path.exists():
        print("❌ Error: PlantVillage dataset not found!")
        print("\nYou need to:")
        print("1. Create PlantVillage folder")
        print("2. Add disease class folders inside")
        print("3. Add images to each folder")
        print("\nSee TRAINING_GUIDE.md for details")
        return False
    
    # Get classes
    classes = [d for d in dataset_path.iterdir() if d.is_dir()]
    
    if not classes:
        print("❌ No class folders found in PlantVillage/")
        return False
    
    print("\n" + "="*70)
    print("🌾 CROP DISEASE MODEL TRAINING")
    print("="*70)
    print(f"\n📂 Dataset: {dataset_path.absolute()}")
    print(f"📊 Classes found: {len(classes)}")
    print(f"🔧 Configuration:")
    print(f"   - Epochs: {args.epochs}")
    print(f"   - Batch size: {args.batch_size}")
    print(f"   - Image size: 224×224px")
    
    # Prepare images if requested
    if args.prepare_images:
        print("\n" + "-"*70)
        print("🔄 Preparing images...")
        print("-"*70)
        try:
            result = subprocess.run(
                [sys.executable, "prepare_images.py", 
                 "--dataset_path", str(dataset_path)],
                check=True
            )
            if result.returncode != 0:
                print("⚠️  Image preparation had issues but continuing...")
        except Exception as e:
            print(f"⚠️  Could not prepare images: {e}")
    
    # Validate dataset only
    if args.validate_only:
        print("\n" + "-"*70)
        print("📊 Validating dataset...")
        print("-"*70)
        try:
            subprocess.run(
                [sys.executable, "prepare_images.py",
                 "--dataset_path", str(dataset_path),
                 "--validate_only"],
                check=True
            )
        except Exception as e:
            print(f"Error during validation: {e}")
        return True
    
    # Run training
    print("\n" + "-"*70)
    print("🎯 Starting training...")
    print("-"*70 + "\n")
    
    try:
        result = subprocess.run(
            [sys.executable, "train_real_model.py",
             "--dataset_path", str(dataset_path),
             "--epochs", str(args.epochs),
             "--batch_size", str(args.batch_size)],
            check=True
        )
        
        if result.returncode == 0:
            print("\n" + "="*70)
            print("✅ TRAINING COMPLETE!")
            print("="*70)
            print("\nNext steps:")
            print("1. Model saved to: model.h5 and saved_model/")
            print("2. Restart Flask: python app.py")
            print("3. Upload crop images to test detection")
            print("4. Check that crop names and remedies display correctly")
            print("\n" + "="*70 + "\n")
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Training failed with error: {e}")
        return False
    except KeyboardInterrupt:
        print("\n⚠️  Training interrupted by user")
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
