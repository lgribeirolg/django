from django.urls import path
from data_science.views import index

urlpatterns = [
        path('', index)
]