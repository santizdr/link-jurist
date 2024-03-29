from django.urls import path
from . import api


urlpatterns = [
    path('index/', api.index, name='index'),
    path('accountdetails/', api.accountdetails, name='accountdetails'),
    path('userdetails/', api.userdetails, name='userdetails'),
    path('createpost', api.createpost, name='createpost'),
    path('editpost/', api.editpost, name='editpost'),
    path('deletepost/', api.deletepost, name='deletepost'),
    path('follow', api.follow, name='follow'),
    path('likepost', api.likepost, name='likepost')
]