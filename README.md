# Tertiary Emotion Detection

A web-based application that analyzes facial expressions in uploaded images to detect complex, tertiary emotions using DeepFace AI for face detection and emotion recognition.

## Features

- **Advanced Face Detection**: Uses DeepFace with multiple face detection backends (RetinaFace, MTCNN, OpenCV, etc.)
- **Tertiary Emotion Inference**: Goes beyond basic emotions to identify complex emotional states like Delight, Contempt, Despair, etc.
- **Modern Full-Stack Architecture**: Flask backend with modern frontend UI
- **Real-time Analysis**: Upload images and get instant emotion analysis results
- **Responsive Design**: Clean, mobile-friendly UI with Tailwind CSS

## Architecture

- **Backend**: Python Flask server with DeepFace integration
- **Frontend**: Modern HTML/JavaScript with Tailwind CSS
- **AI Models**: DeepFace (TensorFlow-based) for emotion detection
- **Communication**: RESTful API with CORS support

## Quick Start

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
pip install tf-keras  # Additional compatibility fix
```

### 2. Start Backend Server
```bash
python app.py
```

### 3. Open Frontend
Open `index.html` in your web browser and start analyzing emotions!

## How It Works

1. **Upload**: Drag and drop or select an image with a face
2. **Backend Processing**: Flask server uses DeepFace to analyze facial expressions
3. **Tertiary Inference**: Algorithm combines top two emotions to determine complex emotional states
4. **Results**: View both primary emotion scores and inferred tertiary emotion

## Tertiary Emotions Detected

- **Delight** (Happy + Surprise)
- **Contentment** (Happy + Neutral)
- **Remorse** (Sad + Disgust)
- **Despair** (Sad + Fear)
- **Bitterness** (Sad + Angry)
- **Contempt** (Angry + Disgust)
- **Awe** (Fear + Surprise)
- **Disappointment** (Neutral + Sad)
- **Apprehension** (Neutral + Fear)

## Technologies Used

- **Backend**: Flask, DeepFace, OpenCV, TensorFlow
- **Frontend**: HTML5, JavaScript ES6+, Tailwind CSS
- **AI Models**: Pre-trained neural networks via DeepFace
- **File Handling**: Multipart form data, canvas for image display

## API Endpoints

- `GET /health` - Server health check
- `POST /analyze` - Image emotion analysis
  - Accepts: `multipart/form-data` with `image` field
  - Returns: JSON with primary emotions and tertiary emotion

## Deployment Options

### Local Development
Use the built-in Flask development server (current setup)

### Production Deployment
- **Frontend**: Deploy `index.html` to any static hosting (Netlify, Vercel, etc.)
- **Backend**: Deploy Flask app to cloud platforms (Heroku, AWS, Google Cloud)
- **Note**: Update `BACKEND_URL` in frontend to match your production backend URL

## Browser Compatibility

Requires a modern browser with support for:
- ES6+ JavaScript features
- Fetch API
- File API
- FormData

## Privacy

All image processing happens on your server infrastructure. Images are processed in memory and not stored permanently.

## Troubleshooting

### Common Issues

1. **"Backend Server Not Running" Error**
   - Ensure Flask server is started: `python app.py`
   - Check server is accessible at `http://localhost:5000/health`

2. **Import/Module Errors**
   - Install all dependencies: `pip install -r requirements.txt`
   - Install tf-keras compatibility: `pip install tf-keras`

3. **First Analysis is Slow**
   - DeepFace downloads models on first use (~100MB)
   - Subsequent analyses are much faster

4. **CORS Issues**
   - Flask-CORS is configured for development
   - For production, configure proper CORS policies