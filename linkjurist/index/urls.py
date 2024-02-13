from django.urls import path
from . import api


urlpatterns = [
    path('index/<int:id>/', api.index, name='index'),
    path('accountdetails/<int:me>/<int:id>/', api.accountdetails, name='accountdetails'),
    path('createpost', api.createpost, name='createpost'),
    path('follow', api.follow, name='follow'),
]