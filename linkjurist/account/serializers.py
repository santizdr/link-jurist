from rest_framework import serializers
from .models import User, Account

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id' ,'email', 'firstname', 'lastname')


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'name', 'web', 'locality')
