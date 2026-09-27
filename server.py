''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
import requests

# Import the sentiment_analyzer function from the package created:
from EmotionDetection.emotion_detection import emotion_detector as detect_emotion

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector():
    '''This code receives the text from the HTML interface and
       runs emotion detection over it using emotion_detector().
    '''

    text_to_analyze = request.args.get("textToAnalyze")

    result = detect_emotion(text_to_analyze)

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
