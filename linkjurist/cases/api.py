from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import CaseForm


@api_view(['POST'])
def postcase(request):
    data = request.data.get('_rawValue')
    print(data)

    cases = []
    message = 'success'
    
    form = CaseForm({
        'account': data.get('account'),
        'title': data.get('title'),
        'description': data.get('description'),
        'type': data.get('type'),
        'expiry_date': data.get('expiryDate'),
        'percent': data.get('percent'),
    })


    print(form.is_valid())
    print(form.errors)

    if form.is_valid():
        form.save()

    else: 
        message = 'error'

    return JsonResponse({
        'message': message,
        'cases': cases,
    })

