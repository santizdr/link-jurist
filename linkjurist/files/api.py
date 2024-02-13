from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from files.models import File
from files.forms import FileForm
from .serializers import FileSerializer


@api_view(['GET'])
def files(request):
    id = request.query_params.get('id')
    files_data = File.objects.all().exclude(id=id)
    files = FileSerializer(files_data, many=True, context={'account': id}).data

    return JsonResponse({
        'files': files
    })


@api_view(['POST'])
def uploadfile(request):
    files = []
    message = 'success'
    form = FileForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()

        files_data = File.objects.filter(account_id=request.data.get('account'))
        files = FileSerializer(files_data, many=True).data

    else: 
        message = 'error'

    return JsonResponse({
        'message': message,
        'files': files,
    })


@api_view(['GET'])
def getfile(request):
    id = request.query_params.get('id')

    file = get_object_or_404(File, id=id)
    return FileResponse(file.file, as_attachment=True, content_type='application/pdf')