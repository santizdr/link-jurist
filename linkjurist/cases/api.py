from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import CaseForm
from .models import Case


@api_view(['POST'])
def postcase(request):
    data = request.data.get('_rawValue')

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

    if form.is_valid():
        form.save()

        cases_data = Case.objects.filter(account_id=data.get('account'))
        for case in cases_data:
            cases.append({
                'id': case.id,
                'title': case.title,
                'description': case.description,
                'type': case.type,
                'postDate': case.post_date,
                'expiryDate': case.expiry_date,
                'applications': case.applitcations,
                'visualizations': case.visualizations,
                'percent': case.percent,
            })

    else: 
        message = 'error'

    return JsonResponse({
        'message': message,
        'cases': cases,
    })

