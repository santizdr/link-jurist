import io
import json
import os
import PyPDF2
import fitz
from django.conf import settings
from django.http import HttpResponse
from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from files.models import File, FileTag
from files.forms import FileForm, EditFileForm
from .serializers import FileSerializer

from tags.models import Tag


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
    print(request.POST)
    print(form.errors)
    if form.is_valid():
        
        tags_str = request.POST.get('tags')
        tags_str = tags_str.strip()
        tags = json.loads(tags_str)

        file = form.save()

        for tag_id in tags:
            filetag = FileTag(file_id=file.id, tag_id=tag_id)
            filetag.save()

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
    account = int(request.query_params.get('account'))

    file = get_object_or_404(File, id=id)

    if file.account.id == account:
        return FileResponse(file.file, as_attachment=True, content_type='application/pdf')
    else: 
        preview = create_preview(file.file)
        return FileResponse(preview, as_attachment=True, content_type='application/pdf')


def create_preview(file):
    file_data = io.BytesIO()
    pdf = fitz.open()

    file_path = os.path.join(settings.MEDIA_ROOT, str(file))
    original_pdf = fitz.open(file_path)

    page = pdf.new_page(width=original_pdf[0].rect.width, height=original_pdf[0].rect.height)
    page.show_pdf_page(page.rect, original_pdf, 0)

    original_pdf.close()

    image_path = os.path.join(settings.MEDIA_ROOT, 'preview-banner.png')
    image = fitz.open(image_path)

    imagen_width = image[0].rect.width * 0.8
    imagen_height = image[0].rect.height * 0.8
    
    page_width = page.rect.width
    page_height = page.rect.height
    x_pos = (page_width - imagen_width) / 2
    y_pos = (page_height - imagen_height) / 2
    
    new_rect = fitz.Rect(x_pos, y_pos, x_pos + imagen_width, y_pos + imagen_height)
    page.insert_image(new_rect, filename=image, overlay=True)
    image.close()

    pdf.save(file_data)
    file_data.seek(0)

    return file_data


@api_view(['POST'])
def searchfiles(request):
    input = request.data.get('_rawValue').get('input')
    files_data = File.objects.filter(title__icontains=input)
    files = FileSerializer(files_data, many=True).data
    
    return JsonResponse({
        'files': files
    })


@api_view(['POST'])
def filterfiles(request):
    locality = request.data.get('_rawValue').get('locality').capitalize()
    speciality = request.data.get('_rawValue').get('speciality')

    files_data = File.objects.all()
    if(locality != ''):
        files_data = files_data.filter(account__locality=locality)
    if(speciality != ''):
        files_data = files_data.filter(tags__id=speciality)

    files = FileSerializer(files_data, many=True).data
    
    return JsonResponse({
        'files': files
    })


@api_view(['POST'])
def deletefile(request):
    message = "error"
    file = []
    id = request.data.get('id')
    file = get_object_or_404(File, id=id)
    account_id = file.account.id

    FileTag.objects.filter(file_id=id).delete()
    file.delete()

    check_deleted = File.objects.filter(id=id)
    if len(check_deleted) == 0:
        message = "success"

    files_data = File.objects.filter(account_id=account_id)
    file = FileSerializer(files_data, many=True).data

    return JsonResponse({
        'message': message,
        'file': file,
    })


@api_view(['POST'])
def editfile(request):
    message = "error"
    data = request.data.get('_rawValue')
    file = File.objects.get(id=data.get('id'))
    account = file.account.id

    form = EditFileForm({
        'title': data.get('title'),
        'description': data.get('description'),
        'price': data.get('price'),
    }, instance=file)

    if form.is_valid():
        file_data = form.save()
        tags = data.get('tags')

        FileTag.objects.filter(file_id=file.id).delete()
        for tag_id in tags:
            filetag = FileTag(file_id=file.id, tag_id=tag_id)
            filetag.save()

        file = FileSerializer(file_data).data
        files_data = File.objects.filter(account_id=account)
        files = FileSerializer(files_data, many=True).data

        message = 'success'

    return JsonResponse({
        'message': message,
        'files' : files,
        'file' : file,
    })
