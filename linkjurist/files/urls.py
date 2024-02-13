from django.urls import path
from . import api

urlpatterns = [
    path('files/', api.files, name='files'),
    path('uploadfile/', api.uploadfile, name='uploadfile'),
    path('getfile/<int:id>/', api.getfile, name='getfile'),
]