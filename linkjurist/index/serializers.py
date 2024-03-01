from rest_framework import serializers
from .models import Post, PostLike


class PostSerializer(serializers.ModelSerializer):
    posted_by_name = serializers.SerializerMethodField()
    account_name = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    def get_posted_by_name(self, obj):
        return obj.posted_by.firstname + " " + obj.posted_by.lastname  

    def get_account_name(self, obj):
        return obj.account.name
    
    def get_likes(self, obj):
        return PostLike.objects.filter(post_id=obj.id).count()
    
    def get_is_liked(self, obj):
        me = self.context.get('me')
        return PostLike.objects.filter(post=obj, user=me).exists()
    
    class Meta:
        model = Post
        fields = '__all__'
