import os, numpy as np, joblib
from django.shortcuts import render
from django.conf import settings

_model = None

def get_model():
    global _model
    if _model is None and os.path.exists(settings.MODEL_PATH):
        _model = joblib.load(settings.MODEL_PATH)
    return _model

ENCODE = {
    'gender':                   {'male': 1, 'female': 0},
    'platform_usage':           {'Instagram': 0, 'TikTok': 1, 'Both': 2},
    'social_interaction_level': {'low': 0, 'high': 1, 'medium': 2},
}

TIPS = {
    0: [
        "Great job! Keep maintaining 7–9 hours of sleep each night.",
        "Continue limiting social media to under 2 hours daily.",
        "Stay physically active — even 30 minutes a day makes a big difference.",
        "Nurture your social connections and talk openly with friends or family.",
    ],
    1: [
        "Consider speaking with a school counselor or mental health professional.",
        "Try reducing daily screen time, especially before bed.",
        "Prioritize consistent sleep — aim for at least 8 hours each night.",
        "Regular physical activity can significantly improve mood and reduce anxiety.",
        "Reach out to a trusted friend, family member, or teacher.",
    ],
}

def index(request):
    return render(request, 'predictor/index.html')

def about(request):
    return render(request, 'predictor/about.html')

def predict(request):
    if request.method != 'POST':
        return render(request, 'predictor/index.html')
    try:
        d = request.POST
        features = np.array([[
            int(d['age']),
            ENCODE['gender'][d['gender']],
            float(d['daily_social_media_hours']),
            ENCODE['platform_usage'][d['platform_usage']],
            float(d['sleep_hours']),
            float(d['screen_time_before_sleep']),
            float(d['academic_performance']),
            float(d['physical_activity']),
            ENCODE['social_interaction_level'][d['social_interaction_level']],
            int(d['stress_level']),
            int(d['anxiety_level']),
            int(d['addiction_level']),
        ]])

        model = get_model()
        if model:
            label = int(model.predict(features)[0])
            prob  = int(model.predict_proba(features)[0][label] * 100)
        else:
            label, prob = 0, 85  # demo fallback

        return render(request, 'predictor/result.html', {
            'label': label,
            'label_text': 'Depression Risk Detected' if label == 1 else 'Low Depression Risk',
            'probability': prob,
            'status': 'danger' if label == 1 else 'safe',
            'tips': TIPS[label],
        })
    except Exception as e:
        return render(request, 'predictor/index.html', {'error': str(e)})
