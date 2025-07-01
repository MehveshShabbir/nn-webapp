# 🚀 Deployment Guide for Neural Network Visualizer

## 📂 Project Structure

```
Neural network web app/
├── app.py              # Streamlit frontend
├── ml_server.py        # Flask backend
├── model.h5           # Trained model
├── requirements.txt   # Python dependencies
├── Procfile          # Deployment configuration
├── runtime.txt       # Python version
└── README.md         # This guide
```

## 🔧 Backend Deployment (Flask API)

### Option 1: Railway (Recommended - Easy & Free)

1. **Create Railway Account**

   - Go to https://railway.app
   - Sign up with GitHub

2. **Deploy Backend**

   ```bash
   # Create a new repository for backend
   mkdir neural-network-backend
   cd neural-network-backend

   # Copy these files:
   cp ml_server.py neural-network-backend/
   cp model.h5 neural-network-backend/
   cp requirements.txt neural-network-backend/
   cp Procfile neural-network-backend/
   cp runtime.txt neural-network-backend/

   # Initialize git
   git init
   git add .
   git commit -m "Initial backend commit"

   # Push to GitHub
   gh repo create neural-network-backend --public
   git remote add origin https://github.com/YOUR_USERNAME/neural-network-backend.git
   git push -u origin main
   ```

3. **Connect to Railway**

   - Go to Railway dashboard
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your `neural-network-backend` repository
   - Railway will auto-deploy!

4. **Get Your Backend URL**
   - After deployment, you'll get a URL like: `https://neural-network-backend-production.up.railway.app`

### Option 2: Heroku

1. **Install Heroku CLI**

   ```bash
   # Linux/WSL
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. **Deploy to Heroku**

   ```bash
   # Login to Heroku
   heroku login

   # Create app
   heroku create your-neural-network-api

   # Deploy
   git add .
   git commit -m "Deploy backend"
   git push heroku main

   # Your backend URL: https://your-neural-network-api.herokuapp.com
   ```

---

## 🎨 Frontend Deployment (Streamlit App)

### Option 1: Streamlit Community Cloud (Recommended - Free)

1. **Prepare Frontend**

   ```bash
   # Create frontend repository
   mkdir neural-network-frontend
   cd neural-network-frontend

   # Copy frontend files
   cp app.py neural-network-frontend/
   cp requirements-frontend.txt neural-network-frontend/requirements.txt
   ```

2. **Create Frontend Requirements**

   ```bash
   # Create requirements-frontend.txt
   echo "streamlit==1.28.0
   requests==2.31.0
   matplotlib==3.7.2
   numpy==1.24.3
   Pillow==10.0.0" > requirements-frontend.txt
   ```

3. **Update Frontend URL**

   - In `app.py`, change:

   ```python
   URI = 'https://your-backend-url-here.railway.app'  # Replace with your backend URL
   ```

4. **Deploy to Streamlit Cloud**

   ```bash
   # Push to GitHub
   git init
   git add .
   git commit -m "Initial frontend commit"
   gh repo create neural-network-frontend --public
   git remote add origin https://github.com/YOUR_USERNAME/neural-network-frontend.git
   git push -u origin main
   ```

5. **Connect to Streamlit Cloud**
   - Go to https://share.streamlit.io
   - Sign in with GitHub
   - Click "New app"
   - Select your `neural-network-frontend` repository
   - Main file: `app.py`
   - Deploy!

### Option 2: Railway (Alternative)

1. **Deploy Frontend to Railway**
   - Create another Railway project
   - Connect your frontend repository
   - Railway will auto-detect Streamlit and deploy

---

## 🌐 Custom Domain Setup

### For Railway:

1. Go to your Railway project settings
2. Click "Domains"
3. Add your custom domain
4. Update DNS records as instructed

### For Streamlit Cloud:

1. Go to app settings
2. Click "Sharing"
3. Add custom domain (Premium feature)

---

## 🔄 Environment Variables

### Backend (Railway/Heroku):

```
PORT=5000
FLASK_ENV=production
```

### Frontend:

```
BACKEND_URL=https://your-backend-url.railway.app
```

---

## 📝 Final Steps

1. **Test Your Deployment**

   - Backend: Visit `https://your-backend-url.com` - should show "Welcome To The Model Server!"
   - Frontend: Visit your Streamlit app URL

2. **Update Frontend Code**

   - Replace `URI = 'http://127.0.0.1:5000'` with your deployed backend URL

3. **Custom Domains** (Optional)
   - Backend: `api.yourname.com`
   - Frontend: `neural-visualizer.yourname.com`

---

## 💡 Pro Tips

- **Backend**: Railway is easier than Heroku (no credit card required)
- **Frontend**: Streamlit Cloud is perfect for demos
- **Monitoring**: Both platforms provide logs and metrics
- **Scaling**: Railway auto-scales, Heroku requires configuration

Your Neural Network Visualizer will be live at:

- **Backend API**: `https://your-backend.railway.app`
- **Frontend App**: `https://your-app.streamlit.app`

🎉 **You're live on the internet!**
