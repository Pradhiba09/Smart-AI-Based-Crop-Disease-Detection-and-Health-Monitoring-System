#!/usr/bin/env python
"""
Train a crop disease detection model using PlantVillage dataset.

How to get the dataset:
1. Download from: https://github.com/spMohanty/PlantVillage-Dataset
   OR
2. Download from Kaggle: https://www.kaggle.com/datasets/arjuntejaswi/plant-village

Extract the dataset, then run:
    python train_real_model.py --dataset_path /path/to/PlantVillage
"""

import os
import argparse
import numpy as np
from pathlib import Path
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import json

def get_classes_from_directory(dataset_path):
    """Extract class names from dataset directory structure."""
    classes = []
    dataset_path = Path(dataset_path)
    
    # Look for subdirectories (class folders)
    for item in sorted(dataset_path.iterdir()):
        if item.is_dir():
            classes.append(item.name)
    
    return classes

def train_model(dataset_path, epochs=20, batch_size=32):
    """Train model on PlantVillage dataset."""
    
    dataset_path = Path(dataset_path)
    
    if not dataset_path.exists():
        print(f"❌ Error: Dataset path not found: {dataset_path}")
        print("\nHow to get the PlantVillage dataset:")
        print("1. GitHub: https://github.com/spMohanty/PlantVillage-Dataset")
        print("2. Kaggle: https://www.kaggle.com/datasets/arjuntejaswi/plant-village")
        print("\nExtract and pass the path to this script.")
        return False
    
    # Get classes from directory
    classes = get_classes_from_directory(dataset_path)
    
    if not classes:
        print(f"❌ No class folders found in {dataset_path}")
        return False
    
    print(f"\n✓ Found {len(classes)} disease classes:")
    for i, cls in enumerate(classes, 1):
        print(f"  {i}. {cls}")
    
    IMG_SIZE = 224
    NUM_CLASSES = len(classes)
    
    # Create data generators with augmentation
    print("\nLoading dataset...")
    
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest',
        validation_split=0.2
    )
    
    try:
        train_generator = train_datagen.flow_from_directory(
            dataset_path,
            target_size=(IMG_SIZE, IMG_SIZE),
            batch_size=batch_size,
            class_mode='categorical',
            subset='training',
            classes=None
        )
        
        validation_generator = train_datagen.flow_from_directory(
            dataset_path,
            target_size=(IMG_SIZE, IMG_SIZE),
            batch_size=batch_size,
            class_mode='categorical',
            subset='validation',
            classes=None
        )
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        print("Make sure your dataset has the structure: dataset_path/class_name/image.jpg")
        return False
    
    # Get actual classes from generator
    classes = list(train_generator.class_indices.keys())
    NUM_CLASSES = len(classes)
    
    print(f"\n📊 Dataset loaded successfully!")
    print(f"   Training samples: {train_generator.samples}")
    print(f"   Validation samples: {validation_generator.samples}")
    
    # Build model
    print("\n🧠 Building model...")
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
        BatchNormalization(),
        MaxPooling2D((2, 2)),
        
        Conv2D(64, (3, 3), activation='relu'),
        BatchNormalization(),
        MaxPooling2D((2, 2)),
        
        Conv2D(128, (3, 3), activation='relu'),
        BatchNormalization(),
        MaxPooling2D((2, 2)),
        
        Conv2D(128, (3, 3), activation='relu'),
        BatchNormalization(),
        MaxPooling2D((2, 2)),
        
        Flatten(),
        Dense(256, activation='relu'),
        Dropout(0.5),
        Dense(128, activation='relu'),
        Dropout(0.3),
        Dense(NUM_CLASSES, activation='softmax')
    ])
    
    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("\nModel architecture:")
    model.summary()
    
    # Train model
    print(f"\n🚀 Training model for {epochs} epochs...")
    history = model.fit(
        train_generator,
        epochs=epochs,
        validation_data=validation_generator,
        verbose=1
    )
    
    # Evaluate
    val_loss, val_accuracy = model.evaluate(validation_generator, verbose=0)
    print(f"\n✓ Validation Accuracy: {val_accuracy*100:.2f}%")
    print(f"✓ Validation Loss: {val_loss:.4f}")
    
    # Save model
    print("\n💾 Saving model...")
    if os.path.exists('saved_model'):
        import shutil
        shutil.rmtree('saved_model')
    
    model.save('saved_model')
    print("✓ Model saved to 'saved_model/' directory")
    
    # Save class mapping
    class_mapping = {i: cls for i, cls in enumerate(classes)}
    with open('class_mapping.json', 'w') as f:
        json.dump(class_mapping, f, indent=2)
    print("✓ Class mapping saved to 'class_mapping.json'")
    
    print("\n" + "="*60)
    print("✅ Training complete! Your Flask app is ready to use.")
    print("="*60)
    print(f"\nDetectable classes ({NUM_CLASSES}):")
    for i, cls in enumerate(classes, 1):
        print(f"  {i}. {cls}")
    
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train crop disease model on PlantVillage dataset')
    parser.add_argument('--dataset_path', type=str, required=True,
                        help='Path to PlantVillage dataset root folder')
    parser.add_argument('--epochs', type=int, default=20,
                        help='Number of training epochs (default: 20)')
    parser.add_argument('--batch_size', type=int, default=32,
                        help='Batch size (default: 32)')
    
    args = parser.parse_args()
    
    success = train_model(args.dataset_path, epochs=args.epochs, batch_size=args.batch_size)
    
    if not success:
        exit(1)
