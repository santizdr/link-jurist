from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path('index/<int:id>/', api.index, name='index'),
    path('accountdetails/<int:id>/', api.accountdetails, name='accountdetails'),
    path('createpost', api.createpost, name='createpost'),
]