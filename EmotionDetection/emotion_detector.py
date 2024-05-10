"""
    This module takes a text as input and returns the emotion of the text as output.
"""
import json
import requests
def emotion_detector(text_to_analyze):
    """ 
        This function is used to analyze the emotion of 
        a given text using the Watson Emotion Analysis API.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/'
    url+= 'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    emotions = {}
    try:
        response = requests.post(url, json = myobj, headers=header, timeout=5)
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        max_score = 0
        max_emotion = ''
        for emotion in emotions:
            if emotions[emotion] > max_score:
                max_score = emotions[emotion]
                max_emotion = str(emotion)
        emotions['dominant_emotion'] = max_emotion
        return emotions

    except:
        emotions = '<b>Invalid text! Please try again!</b>'
        return emotions

