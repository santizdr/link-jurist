from django.urls import path
from . import api


urlpatterns = [
    path('index/', api.index, name='index'),
    path('accountdetails/', api.accountdetails, name='accountdetails'),
    path('createpost', api.createpost, name='createpost'),
    path('follow', api.follow, name='follow'),
]