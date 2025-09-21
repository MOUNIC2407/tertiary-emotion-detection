# Tertiary Emotion Detection

A web-based application that analyzes facial expressions in uploaded images to detect complex, tertiary emotions using AI-powered face detection and emotion recognition.

## Features

- **Real-time Face Detection**: Uses face-api.js for accurate face detection and emotion analysis
- **Tertiary Emotion Inference**: Goes beyond basic emotions to identify complex emotional states like Delight, Contempt, Despair, etc.
- **Modern UI**: Clean, responsive design with Tailwind CSS
- **Drag & Drop Support**: Easy image upload with visual feedback
- **Detailed Analysis**: Shows both primary emotion scores and inferred tertiary emotions

## How It Works

1. Upload an image containing a face (PNG, JPG, or JPEG)
2. The app detects faces using TinyFaceDetector
3. Extracts facial expression data and emotion scores
4. Analyzes the top two emotions to infer a tertiary emotion
5. Displays results with visual overlays and detailed breakdowns

## Tertiary Emotions Detected

- **Delight** (Happy + Surprised)
- **Contentment** (Happy + Neutral)
- **Remorse** (Disgusted + Sad)
- **Despair** (Fearful + Sad)
- **Bitterness** (Angry + Sad)
- **Contempt** (Angry + Disgusted)
- **Awe** (Fearful + Surprised)
- **Disappointment** (Neutral + Sad)
- **Apprehension** (Fearful + Neutral)

## Technologies Used

- **Face-API.js**: Face detection and emotion recognition
- **Tailwind CSS**: Modern styling and responsive design
- **Vanilla JavaScript**: Client-side processing
- **HTML5 Canvas**: Visual overlays and annotations

## Usage

Simply open `index.html` in a modern web browser. The app will:
1. Load the required AI models (may take a moment on first visit)
2. Present an upload interface
3. Process your image and display results

## Deployment

This is a static web application that can be deployed to any static hosting service like:
- Netlify
- Vercel
- GitHub Pages
- AWS S3
- Any web server

## Browser Compatibility

Requires a modern browser with support for:
- ES6+ JavaScript features
- HTML5 Canvas
- File API
- Fetch API

## Privacy

All image processing happens entirely in your browser. No images are uploaded to external servers.