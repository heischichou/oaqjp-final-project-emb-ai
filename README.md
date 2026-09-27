# Emotion Detection Application using Flask and IBM Watson NLP
This project is a web-based emotion detection application that analyzes text statements and identifies the emotions expressed in the text.

The application detects the following emotions:

- Anger
- Disgust
- Fear
- Joy
- Sadness

It also identifies the dominant emotion, which is the emotion with the highest confidence score.

Features

Accepts text input from users through a web interface

Analyzes text for five different emotions

Determines the dominant emotion

Displays emotion confidence scores

Handles blank user input

Returns None values when the emotion detection service returns HTTP status code 400

Includes unit tests for the emotion detection function

Project Structure
final_project/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
└── README.md

Example

For the statement:

I love my life


The application returns emotion scores similar to:

{
    "anger": 0.006274985,
    "disgust": 0.0025598293,
    "fear": 0.009251528,
    "joy": 0.9680386,
    "sadness": 0.049744144,
    "dominant_emotion": "joy"
}


The response is displayed as:

For the given statement, the system response is 'anger': 0.006274985, 'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386 and 'sadness': 0.049744144. The dominant emotion is joy.

Error Handling

The application handles blank input from users.

If the emotion detection service returns an HTTP 400 status code, the emotion_detector() function returns:

{
    "anger": null,
    "disgust": null,
    "fear": null,
    "joy": null,
    "sadness": null,
    "dominant_emotion": null
}

Unit Testing

Unit tests are provided in:

test_emotion_detection.py


The tests verify that the following statements produce the expected dominant emotions:

Statement	Expected Emotion
I am glad this happened	joy
I am really mad about this	anger
I feel disgusted just hearing about this	disgust
I am so sad about this	sadness
I am really afraid that this will happen	fear

The blank-input case is also tested to verify the error-handling behavior.

Run the unit tests with:

python -m unittest test_emotion_detection.py

Running the Application

Start the Flask application with:

python server.py


The application runs on:

http://localhost:5000


Open the URL in a web browser to use the application.

Technologies Used

Python

Flask

HTML

IBM Watson NLP Emotion Detection

Requests

unittest

Author

[Your Name]

License

This project was created for educational purposes as part of an emotion detection application project.
