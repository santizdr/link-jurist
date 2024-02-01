from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from . forms import SignupForm, AccountForm, AddUserForm
from files.forms import FileForm
from .models import User, Account
from cases.models import Case
from files.models import File
from .serializers import UserSerializer, AccountSerializer
from cases.serializers import CaseSerializer
from files.serializers import FileSerializer


@api_view(['GET'])
def me(request):
    my_user = User.objects.get(id=request.user.id)
    print(my_user.account)
    user = UserSerializer(my_user).data

    if my_user.account is None:
        return JsonResponse({
            'user': user,
            'account': '',
            'team': [],
            'cases': [],
            'files': [],
        })
    else:
        my_account = Account.objects.get(id=my_user.account.id)
        account = AccountSerializer(my_account).data
        
        team_data = User.objects.filter(account_id=account['id'])
        team = UserSerializer(team_data, many=True).data

        cases_data = Case.objects.filter(account_id=account['id'])
        cases = CaseSerializer(cases_data, many=True).data

        files_data = File.objects.filter(account_id=account['id'])
        files = FileSerializer(files_data, many=True).data
            
        return JsonResponse({
            'user': user,
            'account': account,
            'team': team,
            'cases': cases,
            'files': files,
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
def adduser(request):
    team = []
    data = request.data.get('_rawValue')

    message = 'success'
    form = AddUserForm({
        'account': data.get('account'),
        'email': data.get('email'),
        'firstname': data.get('firstname'),
        'lastname': data.get('lastname'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    if form.is_valid():
        form.save()

        team_data = User.objects.filter(account_id=data.get('account'))
        team = UserSerializer(team_data, many=True).data

    else: 
        message = 'error'

    return JsonResponse({
            'message': message,
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

