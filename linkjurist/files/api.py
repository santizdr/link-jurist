from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from files.forms import FileForm
from .serializers import FileSerializer
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
        files = FileSerializer(files_data, many=True).data

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