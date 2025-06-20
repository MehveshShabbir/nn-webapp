# Neural Network Visualizer

This project demonstrates a simple neural network for classifying handwritten digits from the MNIST dataset and provides tools to visualize the network's predictions and activations through a web interface.

## Features

- Trains a neural network on the MNIST dataset using TensorFlow/Keras.
- Visualizes sample images and network activations.
- Provides a Flask-based server to serve model predictions and activations.
- Includes a Streamlit web app for interactive visualization.

## Project Structure

- `Neural Network Visualizer.ipynb`: Jupyter notebook containing all steps from data loading to visualization.
- `ml_server.py`: Flask server for serving predictions and activations.
- `app.py`: Streamlit web app for visualization.

## How to Run

1. **Train the Model**

   - Run the notebook `Neural Network Visualizer.ipynb` to train and save the model as `model.h5`.

2. **Start the ML Server**

   - Run the Flask server:
     ```
     python ml_server.py
     ```

3. **Start the Streamlit App**

   - In a new terminal, run:
     ```
     streamlit run app.py
     ```

4. **Use the Web App**
   - Open the Streamlit app in your browser.
   - Click "Get Random Prediction" to view a random MNIST digit and the neural network's activations.

## Requirements

- Python 3.x
- TensorFlow
- NumPy
- Matplotlib
- Flask
- Streamlit
- Requests

Install dependencies with:

```
pip install tensorflow numpy matplotlib flask streamlit requests
```

---
