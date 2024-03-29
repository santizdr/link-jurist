from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path('me', api.me, name='me'),
    path('signup/', api.signup, name='signup'),
    path('account/', api.account, name='account'),
    path('editaccount/', api.editaccount, name='editaccount'),
    path('user/', api.user, name='user'),
    path('deleteuser/', api.deleteuser, name='deleteuser'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('review', api.review, name='review'),
]