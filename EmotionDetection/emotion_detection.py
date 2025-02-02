import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    
    emotions_scores = {}

    if response.status_code == 400:        
        for feeling in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']:
            emotions_scores[feeling] = None
        return emotions_scores

    dominant_emotion = None
    highest_score = 0.0
    for feeling in ['anger', 'disgust', 'fear', 'joy', 'sadness']:
        emotions_scores[feeling] = formatted_response['emotionPredictions'][0]['emotion'][feeling]
        if emotions_scores[feeling] > highest_score:
            dominant_emotion = feeling
            highest_score = emotions_scores[feeling]
    emotions_scores['dominant_emotion'] = dominant_emotion
    return emotions_scores