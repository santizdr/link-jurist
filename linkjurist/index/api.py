from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.db.models import Count, Q, Sum

from .models import Post, PostTag
from .forms import PostForm
from .serializers import PostSerializer

from account.models import Account, User, Follow
from account.serializers import UserSerializer, AccountSerializer, ContactsSerializer, UserDetailsSerializer
from account.forms import FollowForm

from cases.models import Case
from cases.serializers import CaseSerializer

from files.models import File
from files.serializers import FileSerializer

from index.models import Post
from index.serializers import PostSerializer


@api_view(['GET'])
def index(request):
    id = request.query_params.get('id')

    contacts = []
    contact_suggestions = []
    posts = []
    post_suggestions = []

    contact_ids = Follow.objects.filter(follower=id).values_list('following', flat=True)

    suggestions_data = Account.objects.exclude(id__in=contact_ids).exclude(id=id).annotate(num_following=Count('following')).order_by('-num_following')[:5]
    contact_suggestions = ContactsSerializer(suggestions_data, many=True).data
    
    if contact_ids.count() == 0:
        post_suggestions_data = Post.objects.annotate(total_likes=Sum('likes')).order_by('-total_likes')
        post_suggestions = PostSerializer(post_suggestions_data, many=True).data

    else:
        contacts_data = Account.objects.filter(id__in=contact_ids)
        contacts = ContactsSerializer(contacts_data, many=True).data

        posts_data = Post.objects.filter(Q(account__id__in=contact_ids))
        posts = PostSerializer(posts_data, many=True).data


    return JsonResponse({
        "contacts": contacts,
        "contact_suggestions": contact_suggestions,
        "posts": posts,
        "post_suggestions": post_suggestions,
    })


@api_view(['POST'])
def createpost(request):
    data = request.data.get('_rawValue')
    message = 'success'
    
    form = PostForm({
        'account': data.get('account'),
        'posted_by': data.get('posted_by'),
        'content': data.get('content'),
    })

    if form.is_valid():
        post = form.save()
        tags = data.get('tags')
        for tag_id in tags:
            posttag = PostTag(post_id=post.id, tag_id=tag_id)
            posttag.save()

    else: 
        message = 'error'

    posts_data = Post.objects.filter(account_id=data.get('account'))
    posts = PostSerializer(posts_data, many=True).data

    return JsonResponse({
        'message': message,
        'posts': posts,
    })


@api_view(['GET'])
def accountdetails(request):
    id = request.query_params.get('id')
    me = request.query_params.get('me')

    my_account = Account.objects.get(id=id)
    account = AccountSerializer(my_account).data
    
    follow_data = Follow.objects.filter(follower=me, following=id)
    follow = follow_data.exists()

    team_data = User.objects.filter(account_id=id)
    team = UserSerializer(team_data, many=True).data

    posts_data = Post.objects.filter(account_id=account['id'])
    posts = PostSerializer(posts_data, many=True).data
    
    cases_data = Case.objects.filter(account_id=id)
    cases = CaseSerializer(cases_data, many=True,context={'account': me}).data

    files_data = File.objects.filter(account_id=id)
    files = FileSerializer(files_data, many=True).data

    return JsonResponse({
        'account': account,
        'follow': follow,
        'team': team,
        'posts': posts,
        'cases': cases,
        'files': files,
    })


@api_view(['GET'])
def userdetails(request):
    id = request.query_params.get('id')

    my_user = User.objects.get(id=id)
    user = UserDetailsSerializer(my_user).data

    return JsonResponse({
        'user': user,
    })


@api_view(['POST'])
def follow(request):
    message = 'error'
    follower = request.data.get('follower')
    following = request.data.get('following')

    follow = Follow.objects.filter(follower=follower, following=following)

    if follow.exists():
        follow.delete()
        message = 'unfollowed'

    else: 
        form = FollowForm({
            'follower': request.data.get('follower'),
            'following': request.data.get('following'),
        })

        if form.is_valid():
            form.save()
            message = 'followed'

        else: 
            message = 'error'

    return JsonResponse({
        'message': message,
    })



