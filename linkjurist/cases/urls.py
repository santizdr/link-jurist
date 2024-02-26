from django.urls import path
from . import api


urlpatterns = [
    path('postcase/', api.postcase, name='postcase'),
    path('cases/', api.cases, name='cases'),
    path('apply/', api.apply, name='apply'),
    path('assigncase/', api.assigncase, name='assigncase'),
    path('searchcases/', api.searchcases, name='searchcases'),
    path('filtercases/', api.filtercases, name='filtercases'),
    path('deletecase/', api.deletecase, name='deletecase'),
    path('editcase/', api.editcase, name='editcase'),
]