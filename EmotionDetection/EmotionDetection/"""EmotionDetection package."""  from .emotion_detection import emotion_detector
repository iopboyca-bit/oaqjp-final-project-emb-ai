"""Emotion detection using Watson NLP."""

import requests


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion."""
    url = (
        "https://sn-watson-emotion.labs.skills.network"
        "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(
        url, json=payload, headers=headers, timeout=30
    )

    if response.status_code == 400:
        return dict.fromkeys((
            "anger", "disgust", "fear", "joy",
            "sadness", "dominant_emotion"
        ))

    response.raise_for_status()

    emotion = response.json()["emotionPredictions"][0]["emotion"]

    result = {
        key: emotion[key]
        for key in ("anger", "disgust", "fear", "joy", "sadness")
    }
    result["dominant_emotion"] = max(result, key=result.get)

    return result
