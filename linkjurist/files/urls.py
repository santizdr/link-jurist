from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path('uploadfile/', api.uploadfile, name='uploadfile'),
    path('getfile/<int:id>/', api.getfile, name='getfile'),
]