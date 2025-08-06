# rag_app/urls.py
from django.urls import path
from .views import rag_chat

urlpatterns = [
    path('run/', rag_chat, name='rag_chat'),
]
