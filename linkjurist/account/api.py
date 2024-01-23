from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from . forms import SignupForm


@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'email': request.user.email,
        'firstname': request.user.firstname,
        'lastname': request.user.lastname,
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

    print()
    return JsonResponse({'message': message})
