from django.contrib import admin
from django.urls import path, include
from api.views import BookAPIView

urlpatterns = [
    path('', BookAPIView.as_view()),
]