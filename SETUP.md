# Setup and Run Instructions

## Prerequisites

1. **Python 3.8+** installed on your system
2. **pip** (Python package manager)

## Installation Steps

### 1. Set up Python Environment (Recommended)

```bash
# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** The first installation may take several minutes as DeepFace downloads pre-trained models.

## Running the Application

### 1. Start the Backend Server

```bash
python app.py
```

You should see output like:
```
Starting DeepFace server... Open index.html in your browser.
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:5000
* Running on http://[your-ip]:5000
```

### 2. Open the Frontend

Open `index.html` in your web browser. The app will automatically check if the backend server is running.

## Troubleshooting

### Common Issues

1. **"Backend Server Not Running" Error**
   - Make sure you started the Python server (`python app.py`)
   - Check that the server is running on port 5000
   - Look for any error messages in the terminal

2. **Module Import Errors**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check that you're using the correct Python environment

3. **CORS Errors**
   - The flask-cors package should handle this automatically
   - If issues persist, try accessing via `http://localhost` instead of `file://`

4. **Model Download Issues**
   - DeepFace downloads models on first use
   - Ensure you have a stable internet connection
   - Models are cached locally after first download

### Performance Notes

- First analysis may be slower as DeepFace loads models
- Subsequent analyses will be faster
- GPU acceleration is automatic if available (CUDA-compatible GPU + TensorFlow-GPU)

## File Structure

```
Tertiary_emotion/
├── app.py              # Flask backend server
├── index.html          # Frontend application
├── requirements.txt    # Python dependencies
├── netlify.toml       # Netlify deployment config
└── README.md          # Project documentation
```

## API Endpoints

- `GET /health` - Server health check
- `POST /analyze` - Image emotion analysis (expects multipart/form-data with 'image' field)