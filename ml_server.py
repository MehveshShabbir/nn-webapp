import json
import tensorflow as tf
import numpy as np
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["*"])

# Load model and create feature model
try:
    model = tf.keras.models.load_model('model.h5')
    feature_model = tf.keras.models.Model(
        model.inputs,
        [layer.output for layer in model.layers]
    )
    print("✅ Model loaded successfully")
    print(f"Model input shape: {model.input_shape}")
except Exception as e:
    print(f"❌ Model loading error: {e}")
    model = None
    feature_model = None

# Load test data
try:
    _, (x_test, _) = tf.keras.datasets.mnist.load_data()
    x_test = x_test / 255.0
    print("✅ MNIST data loaded successfully")
except Exception as e:
    print(f"❌ MNIST loading error: {e}")
    x_test = None

def get_prediction():
    try:
        if x_test is None:
            raise Exception("MNIST data not loaded")
        if feature_model is None:
            raise Exception("Model not loaded")
            
        # Get random image
        index = np.random.choice(x_test.shape[0])
        image = x_test[index]
        
        # Reshape to model's expected input
        if len(image.shape) == 2:  # (28, 28)
            image_arr = image.reshape(1, 784)
        else:
            image_arr = image.reshape(1, -1)  # fallback
            
        print(f"Input shape for prediction: {image_arr.shape}")
        
        # Validate input shape matches model
        if image_arr.shape[1] != 784:
            raise ValueError(f"Input shape {image_arr.shape} doesn't match expected 784 features")
        
        # Get predictions from all layers
        preds = feature_model.predict(image_arr, verbose=0)
        
        return preds, image
        
    except Exception as e:
        print(f"❌ Prediction error: {e}")
        raise e

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            print("📨 POST request received")
            preds, image = get_prediction()
            
            # Convert to JSON-serializable format
            final_preds = [p.tolist() for p in preds]
            
            response_data = {
                'prediction': final_preds,
                'image': image.tolist()
            }
            
            print("✅ Prediction generated successfully")
            return jsonify(response_data)  # Using jsonify instead of json.dumps
            
        except Exception as e:
            print(f"❌ Error in POST handler: {e}")
            return jsonify({'error': str(e)}), 500
    
    return 'Welcome To The Neural Network API!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"🚀 Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)