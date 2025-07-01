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
    print("✅ Model loaded successfully")
    print("Model input details:")
    print(model.inputs)
    print(f"Expected input shape: {model.input_shape}")
    model.summary()  # Print model architecture
    
    feature_model = tf.keras.models.Model(
        model.inputs,
        [layer.output for layer in model.layers]
    )
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
        if x_test is None or feature_model is None:
            raise Exception("Model or data not loaded properly")
            
        index = np.random.choice(x_test.shape[0])
        image = x_test[index]
        
        # Reshape based on model's expected input
        if len(model.input_shape) == 3:
            # For CNN models expecting (batch, height, width)
            image_arr = image.reshape((1,) + model.input_shape[1:])
        else:
            # For dense models expecting (batch, features)
            image_arr = image.reshape(1, -1)
            
        print(f"Input shape for prediction: {image_arr.shape}")
        
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
            response_data = {
                'prediction': [p.tolist() for p in preds],
                'image': image.tolist()
            }
            return jsonify(response_data)
        except Exception as e:
            print(f"❌ Error in POST handler: {e}")
            return jsonify({'error': str(e)}), 500
    return 'Welcome To The Neural Network API!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)