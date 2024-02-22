from django.urls import path
from . import api


urlpatterns = [
    path('index/', api.index, name='index'),
    path('accountdetails/', api.accountdetails, name='accountdetails'),
    path('userdetails/', api.userdetails, name='userdetails'),
    path('createpost', api.createpost, name='createpost'),
    path('deletepost/', api.deletepost, name='deletepost'),
    path('follow', api.follow, name='follow'),
]