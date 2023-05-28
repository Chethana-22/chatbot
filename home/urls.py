from django.urls import path
from home.views import home, chatAPI

urlpatterns = [
    path('chat', home, name='home'),
    path('api', chatAPI, name='chatAPI'),
]
