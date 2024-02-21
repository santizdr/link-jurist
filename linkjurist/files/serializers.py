from rest_framework import serializers
from .models import File
import os

class FileSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()
    account_name = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = '__all__'

    def get_file_url(self, obj):
        return os.getcwd() + "/media" + obj.file.url
    
    def get_account_name(self, obj):
        return obj.account.name
