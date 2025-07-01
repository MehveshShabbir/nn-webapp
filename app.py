import streamlit as st
import json
import requests
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title='Neural Network Visualizer', 
    layout='wide', 
    initial_sidebar_state='expanded'
)

st.markdown(
    """
    <style>
    header[data-testid="stHeader"] {
        display: none;
    }
    
    body, .stApp {
        background-color: #111111 !important;
        color: #bf40ff !important;
    }
    
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background-color: #111111;
        padding: 10px 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 2px solid #bf40ff;
        box-shadow: 0 0 15px rgba(191, 64, 255, 0.5);
        z-index: 100;
    }
    
    .logo-container {
        display: flex;
        align-items: center;
    }
    
    .navbar img {
        height: 40px;
        margin-right: 10px;
    }
    
    .navbar-title {
        color: #bf40ff !important;
        font-size: 28px !important;
        font-weight: bold !important;
        margin: 0 0 0 0px !important;
        text-shadow: 0 0 10px #00fff7;
        font-family: Arial, sans-serif !important;
    }
    
    .navbar-options {
        display: flex;
        gap: 20px;
    }
    
    .navbar-options a {
        color: #ffffff !important;
        text-decoration: underline !important;
        padding: 8px 16px;
        border-radius: 5px;
        transition: all 0.3s ease;
        font-size: 18px;
    }
    
    .navbar-options a:hover {
        background-color: #bf40ff !important;
        color: #111111 !important;
        box-shadow: 0 0 10px #bf40ff;
        text-decoration: none !important;
    }
    
    .stButton>button {
        background-color: #222222 !important;
        color: #bf40ff !important;
        border: 2px solid #bf40ff !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        box-shadow: 0 0 10px #bf40ff, 0 0 20px #00fff7 !important;
    }
    
    .stButton>button:hover {
        background-color: #bf40ff !important;
        color: #111111 !important;
        box-shadow: 0 0 20px #00fff7, 0 0 40px #bf40ff !important;
    }
    
    .main-content {
        padding-top: 80px !important;
    }
    
    .main-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #bf40ff;
        text-shadow: 0 0 10px #00fff7, 0 0 20px #bf40ff;
        margin: 20px 0 30px 0;
    }
    
    .footer {
        background-color: #222222;
        color: #ffffff;
        text-align: center;
        padding: 10px;
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        width: 100%;
        font-size: 14px;
        box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .digit-image {
        border: 2px solid #bf40ff;
        border-radius: 8px;
        box-shadow: 0 0 15px rgba(191, 64, 255, 0.5);
        margin: 0 auto;
        width: fit-content;
    }
    
    @media (max-width: 768px) {
        .navbar-title {
            font-size: 20px !important;
        }
        .navbar-options a {
            font-size: 14px;
            padding: 6px 12px;
        }
        .main-title {
            font-size: 28px;
        }
        .stMarkdown h2 {
            font-size: 1.2em !important;
        }
    }
    </style>
    
    <div class="navbar">
        <div class="logo-container">
            <img src="https://managementcontainer.blob.core.windows.net/zizzle/logo.jpeg" alt="Logo">
            <div class="navbar-title">NodeSync</div>
        </div>
        <div class="navbar-options">
            <a href="#">Contact</a>
            <a href="#">Profile</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

URI = 'http://127.0.0.1:5000'

st.markdown('<div class="main-title">Neural Network Visualizer</div>', unsafe_allow_html=True)

st.markdown('## Sample Image Analysis')

if st.button('Wanna see how it works?'):
    try:
        response = requests.post(URI, data={})
        response = json.loads(response.text)
        preds = response.get('prediction')
        image = response.get('image')
        image = np.reshape(image, (28, 28))
        
        st.markdown('<div class="digit-image">', unsafe_allow_html=True)
        st.image(image, caption='Random Digit', width=150)
        st.markdown('</div>', unsafe_allow_html=True)
        
        neon_colors = ['#bf40ff', '#00fff7', '#ff00ff', '#fffb00', '#ff0080', 
                      '#00ffea', '#ff2fff', '#00ffb3', '#ff5e00', '#00ffea']
        
        layer_names = ['First Layer (Hidden)', 'Second Layer (Hidden)', 'Output Layer']
        
        for layer, p in enumerate(preds):
            numbers = np.squeeze(np.array(p))
            plt.figure(figsize=(32, 4), facecolor='#111111')
            
            if layer == 2:
                row, col = 1, 10
            else:
                row, col = 2, 16
                
            for i, number in enumerate(numbers):
                plt.subplot(row, col, i+1)
                plt.imshow(number * np.ones((8, 8, 3)).astype('float32'), cmap=None)
                plt.xticks([])
                plt.yticks([])
                plt.gca().set_facecolor('#111111')
                
                border_color = neon_colors[i % len(neon_colors)]
                for spine in plt.gca().spines.values():
                    spine.set_color(border_color)
                    spine.set_linewidth(2)
                
                if layer == 2:
                    plt.xlabel(str(i), fontsize=40, color=border_color, fontweight='bold')
            
            plt.subplots_adjust(wspace=0.05, hspace=0.05)
            plt.tight_layout()
            
            st.markdown(
                f'<span style="color:#fffb00; font-size:2em; text-shadow:0 0 10px #00fff7;">{layer_names[layer]}</span>', 
                unsafe_allow_html=True
            )
            st.pyplot(plt)
            
        plt.close('all')
        
    except Exception as e:
        st.error('An error occurred while fetching prediction. Please ensure the ML server is running and try again.')
else:
    st.markdown(
        '<div style="text-align:center; color:#ff00ff; font-size:1.2em; margin:20px;">🎯 Click the button to generate a random analysis and see the neural network activations!</div>', 
        unsafe_allow_html=True
    )

st.markdown(
    """
    <div class="footer">
        <div style="margin: 0 auto;">© Mehvesh Shabbir 2024-2025 | All Rights Reserved</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.set_option('client.showErrorDetails', False)