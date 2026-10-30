import requests
import json

def set_dominant_emotion(emo_dict):
    dominant_emotion=['None', 0.0]
    for key, value in emo_dict.items():
        if value>dominant_emotion[1]:
            dominant_emotion[0] = key
            dominant_emotion[1] = value
    emo_dict['dominant_emotion'] = dominant_emotion[0]

def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json= { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=input_json, headers=headers)
    response_dict = json.loads(response.text)
    emotion_predictions = response_dict['emotionPredictions'][0]['emotion']
    set_dominant_emotion(emotion_predictions)

    if response.status_code == 200:
        return emotion_predictions
    if response.status_code == 400:
        formated_response = {
                            'anger': None,
                            'disgust': None, 
                            'fear': None, 
                            'joy': None, 
                            'sadness': None, 
                            'dominant_emotion': None}
    return emotion_predictions


if __name__=='__main__':
    emotion_detector("I am so happy I am doing this.")