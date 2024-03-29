from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.db.models import Avg

from .models import User, Account, UserTag, Review
from .forms import SignupForm, AccountForm, AddUserForm, EditUserForm, ReviewForm, ImageForm
from .serializers import UserSerializer, AccountSerializer

from files.models import File
from files.serializers import FileSerializer

from cases.models import Case, Apply
from cases.serializers import CaseSerializer, ApplySerializer

from index.models import Post
from index.serializers import PostSerializer


@api_view(['GET'])
def me(request):
    my_user = User.objects.get(id=request.user.id)
    user = UserSerializer(my_user).data

    if my_user.account is None:
        return JsonResponse({
            'user': user,
            'account': '',
            'team': [],
            'posts': [],
            'cases': [],
            'files': [],
            'applications': []
        })
    else:
        my_account = Account.objects.get(id=my_user.account.id)
        account = AccountSerializer(my_account).data
        
        team_data = User.objects.filter(account_id=account['id'])
        team = UserSerializer(team_data, many=True).data

        posts_data = Post.objects.filter(account_id=account['id'])
        posts = PostSerializer(posts_data, many=True).data

        cases_data = Case.objects.filter(account_id=account['id'])
        cases = CaseSerializer(cases_data, many=True).data
        case_ids = [case['id'] for case in cases]

        files_data = File.objects.filter(account_id=account['id'])
        files = FileSerializer(files_data, many=True).data

        applications_data = Apply.objects.filter(case_id__in=case_ids) | Apply.objects.filter(applicant=my_account)
        applications = ApplySerializer(applications_data, many=True).data

        return JsonResponse({
            'user': user,
            'account': account,
            'team': team,
            'posts': posts,
            'cases': cases,
            'files': files,
            'applications': applications
        })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data.get('_rawValue')
    message = 'success'
    form = SignupForm({
        'email': data.get('email'),
        'firstname': data.get('firstname'),
        'lastname': data.get('lastname'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    if form.is_valid():
        form.save()

        # SEND VERIFICATION EMAIL LATER
    else: 
        message = 'error'

    return JsonResponse({'message': message})


@api_view(['POST'])
def user(request):
    message = "success"
    team = []
    user = ""
    data = request.data.get('_rawValue')
    user_id = data.get('id')
    if user_id is None:
        form = AddUserForm({
            'account': data.get('account'),
            'email': data.get('email'),
            'firstname': data.get('firstname'),
            'lastname': data.get('lastname'),
            'description': data.get('description'),
            'password1': data.get('password1'),
            'password2': data.get('password2'),
        })
    else:
        user = User.objects.get(id=data.get('id'))
        data.pop('user', None)
        form = EditUserForm({
            'account': data.get('account'),
            'email': data.get('email'),
            'firstname': data.get('firstname'),
            'lastname': data.get('lastname'),
            'description': data.get('description'),
        }, instance=user)

    if form.is_valid():
        user_data = form.save()
        user_id = user_data.id
        tags = data.get('tags')
        
        if user != "":
            UserTag.objects.filter(user_id=user_id).delete()

        for tag_id in tags:
            usertag = UserTag(user_id=user_id, tag_id=tag_id)
            usertag.save()

        user = UserSerializer(user_data).data
        team_data = User.objects.filter(account_id=data.get('account'))
        team = UserSerializer(team_data, many=True).data
    else: 
        message = 'error'

    return JsonResponse({
        'message': message,
        'user': user,
        'team': team,
    })


@api_view(['POST'])
def account(request):
    team = []
    files = []

    data = request.data.get('_rawValue')
    user = User.objects.get(id=data.get('user'))
    data.pop('user', None)
    message = 'success'
    form = AccountForm({
        'name': data.get('name'),
        'description': data.get('description'),
        'slogan': data.get('slogan'),
        'web': data.get('web'),
        'email': data.get('email'),
        'phonenumber': data.get('phonenumber'),
        'address': data.get('address'),
        'cp': data.get('cp'),
        'locality': data.get('locality'),
        'country': data.get('country'),
    })

    if form.is_valid():
        my_account = form.save()
        account = AccountSerializer(my_account).data

        user.account = my_account
        user.is_manager = True
        user.save()

        team_data = User.objects.filter(account_id=account['id'])
        team = UserSerializer(team_data, many=True).data

    else: 
        message = 'error'

    return JsonResponse({
        'message': message, 
        'account': account,
        'team': team,
        'files': files,
    })


@api_view(['POST'])
def deleteuser(request):
    team = []
    id = request.data.get('id')
    user = get_object_or_404(User, id=id)
    account_id = user.account.id
    manager_id = User.objects.filter(account_id=account_id).filter(is_manager=True)[0]

    Post.objects.filter(posted_by=user).update(posted_by_id=manager_id)
    File.objects.filter(uploaded_by=user).update(uploaded_by=manager_id)
    UserTag.objects.filter(user_id=user).delete()

    user.delete()
    message = 'success'

    team_data = User.objects.filter(account_id=account_id)
    team = UserSerializer(team_data, many=True).data

    return JsonResponse({
        'message': message,
        'team': team,
    })


@api_view(['POST'])
def editaccount(request):
    data = request.data.get('_rawValue')
    account = Account.objects.get(id=data.get('account'))
    data.pop('account', None)
    message = 'success'

    form = AccountForm(
        {
            'name': data.get('name'),
            'description': data.get('description'),
            'slogan': data.get('slogan'),
            'web': data.get('web'),
            'email': data.get('email'),
            'phonenumber': data.get('phonenumber'),
            'address': data.get('address'),
            'cp': data.get('cp'),
            'locality': data.get('locality'),
            'country': data.get('country'),
        }, 
        instance=account
    )

    if form.is_valid():
        my_account = form.save()
        account = AccountSerializer(my_account).data

    message = 'success'

    return JsonResponse({
        'message': message,
        'account' : account,
    })


@api_view(['POST'])
def review(request):
    data = request.data.get('_rawValue')
    message = 'success'
    review = Review.objects.filter(posted_by=data.get('posted_by')).filter(posted_to=data.get('account'))
    rating = Review.objects.filter(posted_to=data.get('account')).aggregate(avg_rating=Avg('rating'))['avg_rating']
    if (rating is not None):
        rating = round(rating)

    if review.exists():
        form = ReviewForm({
            'posted_by': data.get('posted_by'),
            'posted_to': data.get('account'),
            'rating': data.get('rating'),
        }, instance=review[0])

    else: 
        form = ReviewForm({
            'posted_by': data.get('posted_by'),
            'posted_to': data.get('account'),
            'rating': data.get('rating'),
        })
        
    if form.is_valid():
        form.save()
        rating = round(Review.objects.filter(posted_to=data.get('account')).aggregate(avg_rating=Avg('rating'))['avg_rating'])

    else: 
        message = "error"

    return JsonResponse({
        'message': message,
        'rating': rating,
    })
