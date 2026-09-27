Emotion Detection Application
Project Name

Emotion Detection from Text using Flask and IBM Watson NLP

Project Description

This project is a web-based emotion detection application that analyzes a given text statement and identifies the emotions expressed in the text.

The application uses an emotion detection service to determine the following emotions:

Anger

Disgust

Fear

Joy

Sadness

The application also identifies the dominant emotion, which is the emotion with the highest confidence score.

Features

Accepts text input from users through a web interface.

Analyzes the text for five different emotions.

Determines the dominant emotion.

Displays the emotion confidence scores.

Provides error handling for blank user input.

Returns None values when the emotion detection service returns HTTP status code 400.

Includes unit tests for the emotion detection function.

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


the application returns emotion scores similar to:

{
    "anger": 0.006274985,
    "disgust": 0.0025598293,
    "fear": 0.009251528,
    "joy": 0.9680386,
    "sadness": 0.049744144,
    "dominant_emotion": "joy"
}


The application displays the result in the following format:

For the given statement, the system response is 'anger': 0.006274985, 'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386 and 'sadness': 0.049744144. The dominant emotion is joy.

Error Handling

The application handles blank input from users.

If the emotion detection service returns an HTTP 400 status code, the emotion_detector() function returns:

{
    "anger": None,
    "disgust": None,
    "fear": None,
    "joy": None,
    "sadness": None,
    "dominant_emotion": None
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

Run the tests with:

python -m unittest test_emotion_detection.py

Running the Application

Start the Flask application with:

python server.py


The application runs on:

http://localhost:5000


The application can then be accessed through a web browser.

Technologies Used

Python

Flask

HTML

IBM Watson NLP emotion detection service

Requests

unittest

Author

[Your Name]

License

This project was created for educational purposes as part of an emotion detection application project.
