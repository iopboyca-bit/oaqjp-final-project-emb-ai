"""Flask server for the emotion detection application."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detection():
    """Detect emotions and handle invalid input."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """Render the application home page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
