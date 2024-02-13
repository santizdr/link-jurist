from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    posted_by_name = serializers.SerializerMethodField()
    account_name = serializers.SerializerMethodField()

    def get_posted_by_name(self, obj):
        return obj.posted_by.firstname + " " + obj.posted_by.lastname  

    def get_account_name(self, obj):
        return obj.account.name
    class Meta:
        model = Post
        fields = '__all__'
