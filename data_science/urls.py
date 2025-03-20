from django.urls import path
from data_science.views import index,imagem

urlpatterns = [
        path('', index),
        path('imagem/',imagem)
]