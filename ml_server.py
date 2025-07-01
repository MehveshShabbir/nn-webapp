import json
import tensorflow as tf
import numpy as np
import random
import os
from flask import Flask, request
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
model=tf.keras.models.load_model('model.h5')
feature_model=tf.keras.models.Model(
    model.inputs,
    [layer.output for layer in model.layers]
)
_, (x_test, _) = tf.keras.datasets.mnist.load_data()
x_test = x_test / 255.
x_test = np.reshape(x_test, (x_test.shape[0], 784))
def get_prediction():
    index = np.random.choice(x_test.shape[0])
    image = x_test[index, :]
    image_arr = np.reshape(image, (1, 1, 784))
    return feature_model.predict(image_arr), image.reshape(28, 28)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        preds, image=get_prediction()
        final_preds=[p.tolist() for p in preds]
        return json.dumps({
            'prediction': final_preds,
            'image':image.tolist()
        })
    return 'Welcome To The Model Server!'
@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    image = np.array(data['image']).reshape(1, 1, 784)
    preds = feature_model.predict(image)
    confidence = np.max(preds[-1]) * 100
    final_preds = [p.tolist() for p in preds]
    return json.dumps({
        'prediction': final_preds,
        'confidence': confidence
    })
if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
