from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from . forms import SignupForm, AccountForm
from .models import User, Account


@api_view(['GET'])
def me(request):
    user = User.objects.get(id=request.user.id)
    if user.account is None:
        return JsonResponse({
            'user': {
                'id': request.user.id,
                'email': request.user.email,
                'firstname': request.user.firstname,
                'lastname': request.user.lastname,
            },
            'account': '',
        })
    else:
        account = Account.objects.get(id=user.account.id)
        return JsonResponse({
            'user': {
                'id': request.user.id,
                'email': request.user.email,
                'firstname': request.user.firstname,
                'lastname': request.user.lastname,
            },
            'account': {
                'name': account.name,
                'description': account.description,
                'slogan': account.slogan,
                'email': account.email,
                'web': account.web,
                'phonenumber': account.phonenumber,
                'address': account.address,
                'cp': account.cp,
                'locality': account.locality,
                'country': account.country,
            },
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
def account(request):
    data = request.data.get('_rawValue')
    user = User.objects.get(id=data.get('user'))
    data.pop('user', None)
    print(data)
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
        account = form.save()
        user.account = account
        user.save()
        # SEND VERIFICATION EMAIL LATER
    else: 
        message = 'error'

    return JsonResponse({
        'message': message, 
        'account': 
            {
                'name': account.name,
                'description': account.description,
                'slogan': account.slogan,
                'email': account.email,
                'web': account.web,
                'address': account.address,
                'cp': account.cp,
                'locality': account.locality,
                'country': account.country,
                }
    })