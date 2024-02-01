from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from files.forms import FileForm
from .models import User, Account
from files.models import File


@api_view(['POST'])
def uploadfile(request):
    account = request.data.get('account')[0]
    files = []
    message = 'success'
    form = FileForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()

        files_data = File.objects.filter(account_id=account)
        for file in files_data:
            files.append({
                'id': file.id,
                'title': file.title,
                'description': file.description,
                'price': file.price,
                'downloads': file.downloads,
                'account': file.account.id,
                'uploaded_by': file.uploaded_by.id,
            })

    else: 
        message = 'error'

    return JsonResponse({
        'message': message,
        'files': files,
    })


@api_view(['GET'])
def getfile(request, id):
    file = get_object_or_404(File, id=id)
    return FileResponse(file.file, as_attachment=True, content_type='application/pdf')