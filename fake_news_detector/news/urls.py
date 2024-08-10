from django.urls import path
from .views import index, predict

urlpatterns = [
    path('', index, name='index'),  # This will be accessed at /news/
    path('predict/', predict, name='predict'),  # This will be accessed at /news/predict/
]
