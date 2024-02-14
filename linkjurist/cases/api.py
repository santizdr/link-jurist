from datetime import date
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import CaseForm, ApplyForm
from .models import Case, Apply
from .serializers import ApplySerializer, CaseSerializer


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
        cases = CaseSerializer(cases_data, many=True).data

    else: 
        message = 'error'

    return JsonResponse({
        'message': message,
        'cases': cases,
    })


@api_view(['GET'])
def cases(request):
    id = request.query_params.get('id')
    cases_data = Case.objects.filter(expiry_date__gt=date.today())
    cases = CaseSerializer(cases_data, many=True, context={'account': id}).data

    return JsonResponse({
        'cases': cases
    })


@api_view(['POST'])
def apply(request):
    message = 'error'
    case_id = request.data.get('case')
    applicant = request.data.get('applicant')

    apply = Apply.objects.filter(case=case_id, applicant=applicant)

    if apply.exists():
        apply.delete()
        message = 'delete'

    else: 
        form = ApplyForm({
            'case': case_id,
            'applicant': applicant,
        })

        if form.is_valid():
            form.save()
            message = 'applied'

            case = Case.objects.get(id=case_id)
            case.applications += case.applications
            case.save()

        else: 
            message = 'error'

    return JsonResponse({
        'message': message,
    })


@api_view(['POST'])
def assigncase(request):
    data = request.data.get('_rawValue')
    message = 'error'

    application = Apply.objects.get(id=data.get('id'))
    previous_status = application.status
    application.status = data.get('status')
    application.save()

    if(previous_status != application.status):
        message = 'success'

        cases_data = Case.objects.filter(account_id=data.get('account'))
        cases = CaseSerializer(cases_data, many=True).data
        case_ids = [case['id'] for case in cases]
        
        applications_data = Apply.objects.filter(case_id__in=case_ids)
        applications = ApplySerializer(applications_data, many=True).data

    return JsonResponse({
        'message': message,
        'applications': applications
    })
