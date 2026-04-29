#!/usr/bin/env python
"""
Convert Model.h5 to SavedModel format.
Run this script on a machine where Model.h5 loads successfully.
"""
import os

try:
    from tensorflow.keras.models import load_model as tf_load
    print("Using tensorflow.keras")
    loader = tf_load
except Exception:
    try:
        from keras.models import load_model as keras_load
        print("Using standalone keras")
        loader = keras_load
    except Exception as e:
        print("Error: Could not import either tensorflow.keras or standalone keras")
        print(f"Details: {e}")
        exit(1)

try:
    print("Attempting to load Model.h5...")
    model = loader('Model.h5', compile=False)
    print("✓ Model loaded successfully")
    
    # Save as SavedModel
    if not os.path.exists('saved_model'):
        os.makedirs('saved_model')
    
    model.save('saved_model')
    print("✓ Model saved to 'saved_model/' directory")
    print("\nConversion complete! You can now use TensorFlow's SavedModel API to load:")
    print("  import tensorflow as tf")
    print("  model = tf.saved_model.load('saved_model')")
    
except Exception as e:
    print(f"✗ Error during conversion: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
