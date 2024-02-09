from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path('postcase/', api.postcase, name='postcase'),
    path('cases/', api.cases, name='cases'),
    path('apply/', api.apply, name='apply'),
]