from rest_framework import serializers
from django.db.models import Avg
from .models import User, Account, Review
from index.models import Post
from index.serializers import PostSerializer
from files.models import File
from files.serializers import FileSerializer


class UserSerializer(serializers.ModelSerializer):
    account_name = serializers.SerializerMethodField()
    is_manager = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id' ,'email', 'firstname', 'lastname', 'description', 'tags', 'account', 'account_name', 'is_manager')

    def get_account_name(self, obj):
        if obj.account is not None:
            return obj.account.name
        
    def get_is_manager(self, obj):
            return obj.is_manager
    

class AccountSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = '__all__'

    def get_rating(self, obj):
        rating = Review.objects.filter(posted_to=obj).aggregate(avg_rating=Avg('rating'))
        return rating['avg_rating']    
    

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'name', 'web', 'locality')


class UserDetailsSerializer(serializers.ModelSerializer):
    account_name = serializers.SerializerMethodField()
    posts = serializers.SerializerMethodField()
    files = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id' ,'email', 'firstname', 'lastname', 'description', 'tags', 'account', 'account_name', 'posts', 'files')

    def get_account_name(self, obj):
        return obj.account.name
    
    def get_posts(self, obj):
        posts_data = Post.objects.filter(posted_by=obj.id)
        posts = PostSerializer(posts_data, many=True).data

        return posts
    
    def get_files(self, obj):
        files_data = File.objects.filter(uploaded_by=obj.id)
        files = FileSerializer(files_data, many=True).data

        return files