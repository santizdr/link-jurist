from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.db.models import Count, Q, Sum

from .models import Post
from .forms import PostForm
from .serializers import PostSerializer

from account.models import Account, User, Follow
from account.serializers import UserSerializer, AccountSerializer, ContactsSerializer

from cases.models import Case
from cases.serializers import CaseSerializer

from files.models import File
from files.serializers import FileSerializer


@api_view(['GET'])
def index(request, id):

    contacts = []
    contact_suggestions = []
    publications = []
    publication_suggestions = []

    account = Account.objects.get(id=id)
    contact_ids = Follow.objects.filter(follower=id).values_list('following', flat=True)

    if contact_ids.count() == 0:
        suggestions_data = Account.objects.exclude(id=id).annotate(num_following=Count('following')).order_by('-num_following')[:5]
        contact_suggestions = ContactsSerializer(suggestions_data, many=True).data

        publication_suggestions_data = Post.objects.annotate(total_likes=Sum('likes')).order_by('-total_likes')
        publication_suggestions = PostSerializer(publication_suggestions_data, many=True).data

    else:
        contacts_data = Account.objects.filter(locality=account.locality).exclude(id=id)[:5]
        contacts = ContactsSerializer(contacts_data, many=True).data

        publications_data = Post.objects.filter(Q(account__id__in=contact_ids))
        publications = PostSerializer(publications_data, many=True).data


    return JsonResponse({
        "contacts": contacts,
        "contact_suggestions": contact_suggestions,
        "publications": publications,
        "publication_suggestions": publication_suggestions,
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
        form.save()

    else: 
        message = 'error'

    return JsonResponse({
        'message': message,
    })


@api_view(['GET'])
def accountdetails(request, id):
    my_account = Account.objects.get(id=id)
    account = AccountSerializer(my_account).data
    
    team_data = User.objects.filter(account_id=id)
    team = UserSerializer(team_data, many=True).data

    cases_data = Case.objects.filter(account_id=id)
    cases = CaseSerializer(cases_data, many=True).data

    files_data = File.objects.filter(account_id=id)
    files = FileSerializer(files_data, many=True).data

    print(account)
    print(team)
    print(cases)
    print(files)

    return JsonResponse({
        'account': account,
        'team': team,
        'cases': cases,
        'files': files,
    })
