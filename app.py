# Tertiary Emotion Detection Back-End Server using DeepFace
# Production-ready version for Render deployment

import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from deepface import DeepFace
import cv2
import numpy as np
import traceback

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Tertiary Emotion Mapping
TERTIARY_EMOTIONS = {
    ("happy", "surprise"): "Delight",
    ("happy", "neutral"): "Contentment",
    ("sad", "disgust"): "Remorse",
    ("sad", "fear"): "Despair",
    ("sad", "angry"): "Bitterness",
    ("angry", "disgust"): "Contempt",
    ("fear", "surprise"): "Awe",
    ("neutral", "sad"): "Disappointment",
    ("neutral", "fear"): "Apprehension",
}

def get_tertiary_emotion(emotion_scores):
    """
    Infers a tertiary emotion based on the top two primary emotion scores.
    """
    sorted_emotions = sorted(emotion_scores.items(), key=lambda item: item[1], reverse=True)
    top_emotion_1 = sorted_emotions[0][0]
    top_emotion_2 = sorted_emotions[1][0]

    if (top_emotion_1, top_emotion_2) in TERTIARY_EMOTIONS:
        return TERTIARY_EMOTIONS[(top_emotion_1, top_emotion_2)]
    elif (top_emotion_2, top_emotion_1) in TERTIARY_EMOTIONS:
        return TERTIARY_EMOTIONS[(top_emotion_2, top_emotion_1)]
    else:
        return "Complex or Ambiguous Emotion"

@app.route('/')
def home():
    """
    Root endpoint - returns API info
    """
    return jsonify({
        'message': 'Tertiary Emotion Detection API',
        'status': 'running',
        'endpoints': {
            '/health': 'GET - Health check',
            '/analyze': 'POST - Analyze image for emotions'
        }
    })

@app.route('/health', methods=['GET'])
def health_check():
    """
    Simple health check endpoint to verify the server is running.
    """
    return jsonify({
        'status': 'Server is running', 
        'message': 'DeepFace backend is ready'
    })

@app.route('/analyze', methods=['POST'])
def analyze_image_for_emotions():
    """
    Analyzes an uploaded image to detect primary and tertiary emotions.
    """
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400

        image_file = request.files['image']

        # Read the image file
        filestr = image_file.read()
        npimg = np.frombuffer(filestr, np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        if img is None:
            return jsonify({'error': 'Could not read the image file.'}), 400

        # Use DeepFace to analyze the image
        analysis = DeepFace.analyze(
            img_path=img, 
            actions=['emotion'], 
            enforce_detection=False
        )
        
        if isinstance(analysis, list) and len(analysis) > 0:
            face_analysis = analysis[0]
            emotions = face_analysis['emotion']
            dominant_emotion = face_analysis['dominant_emotion']
            
            # Convert to serializable format
            emotions_serializable = {
                emotion: float(score) 
                for emotion, score in emotions.items()
            }
            
            # Infer tertiary emotion
            tertiary_emotion = get_tertiary_emotion(emotions)

            response_data = {
                'dominant_emotion': dominant_emotion,
                'tertiary_emotion': tertiary_emotion,
                'primary_emotions': emotions_serializable
            }
            
            return jsonify(response_data)
        else:
            return jsonify({'error': 'Could not find a face in the image.'}), 400

    except Exception as e:
        print("An error occurred during analysis:")
        print(traceback.format_exc())
        return jsonify({'error': f'An internal server error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Get port from environment variable (Render sets this)
    port = int(os.environ.get('PORT', 5000))
    # Run in production mode
    app.run(debug=False, host='0.0.0.0', port=port)