from django.urls import path
from .views import chat_api, test_chat_view

urlpatterns = [
    path('api/chat/', chat_api, name='chat_api'),
    path('chat/', test_chat_view, name='test_chat'),
] 