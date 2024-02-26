from django.urls import path
from . import api

urlpatterns = [
    path('files/', api.files, name='files'),
    path('uploadfile/', api.uploadfile, name='uploadfile'),
    path('getfile/', api.getfile, name='getfile'),
    path('searchfiles/', api.searchfiles, name='searchfiles'),
    path('filterfiles/', api.filterfiles, name='filterfiles'),
    path('editfile/', api.editfile, name='editfile'),
    path('deletefile/', api.deletefile, name='deletefile'),
]