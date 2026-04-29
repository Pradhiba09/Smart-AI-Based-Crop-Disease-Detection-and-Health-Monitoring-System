#!/usr/bin/env python
"""
Create a simple crop disease classification model for demo purposes.
This generates synthetic training data and trains a small CNN.
"""
import os
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from disease_info import DISEASE_INFO

# Get disease classes
CLASS_NAMES = list(DISEASE_INFO.keys())
NUM_CLASSES = len(CLASS_NAMES)
IMG_SIZE = 224

print(f"Creating model for {NUM_CLASSES} disease classes:")
for i, cls in enumerate(CLASS_NAMES):
    print(f"  {i+1}. {cls}")

# Create a simple CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    MaxPooling2D((2, 2)),
    
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    
    Conv2D(64, (3, 3), activation='relu'),
    
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(NUM_CLASSES, activation='softmax')
])

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("\nModel architecture:")
model.summary()

# Generate synthetic training data
print("\nGenerating synthetic training data...")
num_samples_per_class = 50
X_train = []
y_train = []

for class_idx in range(NUM_CLASSES):
    # Create random 224x224 RGB images
    for _ in range(num_samples_per_class):
        # Random image (simulating different leaf images)
        img = np.random.rand(IMG_SIZE, IMG_SIZE, 3).astype(np.float32) * 255
        X_train.append(img)
        
        # One-hot encoded label
        label = np.zeros(NUM_CLASSES)
        label[class_idx] = 1
        y_train.append(label)

X_train = np.array(X_train, dtype=np.float32) / 255.0
y_train = np.array(y_train, dtype=np.float32)

print(f"Training data shape: {X_train.shape}")
print(f"Training labels shape: {y_train.shape}")

# Train the model
print("\nTraining model (this may take a minute)...")
model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=32,
    verbose=1,
    validation_split=0.2
)

# Save as SavedModel
print("\nSaving model as SavedModel...")
if os.path.exists('saved_model'):
    import shutil
    shutil.rmtree('saved_model')

model.save('saved_model')
print("✓ Model saved to 'saved_model/' directory")
print("\nYour Flask app should now work! Run:")
print("  python app.py")
