import requests
import json

url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''

    payload = { "raw_document": { "text": text_to_analyze } }
    res = requests.post(url, json=payload, headers=headers)

    if res.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    formatted_json = json.loads(res.text)
    emotions = formatted_json["emotionPredictions"][0]["emotion"]

    response = {}
    dominant_emotion = ''
    max_value = 0

    for key, value in emotions.items():
        response[key] = value

        if value > max_value:
            dominant_emotion = key
            max_value = value

    response["dominant_emotion"] = dominant_emotion

    return response