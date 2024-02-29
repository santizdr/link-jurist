from datetime import date
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import CaseForm, ApplyForm, EditCaseForm
from .models import Case, Apply, CaseTag
from .serializers import ApplySerializer, CaseSerializer

from account.models import Account


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
    })

    if form.is_valid():
        case = form.save()
        tags = data.get('tags')

        for tag_id in tags:
            casetag = CaseTag(case_id=case.id, tag_id=tag_id)
            casetag.save()

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


@api_view(['POST'])
def searchcases(request):
    input = request.data.get('_rawValue').get('input')
    cases_data = Case.objects.filter(expiry_date__gt=date.today(), title__icontains=input)
    cases = CaseSerializer(cases_data, many=True).data
    
    return JsonResponse({
        'cases': cases
    })


@api_view(['POST'])
def filtercases(request):
    type = request.data.get('_rawValue').get('type')
    locality = request.data.get('_rawValue').get('locality').capitalize()
    speciality = request.data.get('_rawValue').get('speciality')

    cases_data = Case.objects.all()
    if(type != ''):
        cases_data = cases_data.filter(type=type)
    if(locality != ''):
        cases_data = cases_data.filter(account__locality=locality)
    if(speciality != ''):
        cases_data = cases_data.filter(tags__id=speciality)

    cases = CaseSerializer(cases_data, many=True).data
    
    return JsonResponse({
        'cases': cases
    })


@api_view(['POST'])
def deletecase(request):
    message = "error"
    case = []
    id = request.data.get('id')
    case = get_object_or_404(Case, id=id)
    account_id = case.account.id

    CaseTag.objects.filter(case_id=id).delete()
    case.delete()

    check_deleted = Case.objects.filter(id=id)
    if len(check_deleted) == 0:
        message = "success"

    cases_data = Case.objects.filter(account_id=account_id)
    case = CaseSerializer(cases_data, many=True).data

    return JsonResponse({
        'message': message,
        'case': case,
    })


@api_view(['POST'])
def editcase(request):
    message = "error"
    data = request.data.get('_rawValue')
    case = Case.objects.get(id=data.get('id'))
    account = case.account.id

    form = EditCaseForm({
        'title': data.get('title'),
        'description': data.get('description'),
        'type': data.get('type'),
        'expiry_date': data.get('expiryDate'),
    }, instance=case)

    if form.is_valid():
        case_data = form.save()
        tags = data.get('tags')

        CaseTag.objects.filter(case_id=case.id).delete()
        for tag_id in tags:
            casetag = CaseTag(case_id=case.id, tag_id=tag_id)
            casetag.save()

        case = CaseSerializer(case_data).data
        cases_data = Case.objects.filter(account_id=account)
        cases = CaseSerializer(cases_data, many=True).data

        message = 'success'

    return JsonResponse({
        'message': message,
        'cases' : cases,
        'case' : case,
    })
