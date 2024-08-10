import joblib
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Load the model and vectorizer
model = joblib.load('news/model/fake_news_model.pkl')
vectorizer = joblib.load('news/model/tfidf_vectorizer.pkl')

def index(request):
    return render(request, 'news/index.html')

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            news_text = data.get('text', '')
            transformed_text = vectorizer.transform([news_text])
            prediction = model.predict(transformed_text)
            return JsonResponse({'prediction': prediction[0]})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def home(request):
    return render(request, 'home.html')
