"""
This module provides endpoints for Emotion Detection
Functions:
- sent_analyzer: Send text for emotion Detection
- render_index_page: Render index page
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    """Send text for emotion detection"""
    text_to_analyze = request.args.get('textToAnalyze')

    if text_to_analyze is None:
        return "Blank text! Try again."

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    emotions_only = ", ".join(f"'{k}': {v}" for k, v in response.items() if k != "dominant_emotion")
    ret = f"For the given statement, the system response is {emotions_only}."
    ret = ret + f" The dominant emotion is <b>{response['dominant_emotion']}</b>."
    return ret

@app.route("/")
def render_index_page():
    """Render index page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
