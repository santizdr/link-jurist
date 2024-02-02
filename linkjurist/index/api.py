from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Count, Q, Sum
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from account.models import Account, Follow
from account.serializers import ContactsSerializer
from .models import Post


@api_view(['GET'])
def index(request, id):

    contacts = []
    contact_suggestions = []
    publications = []
    publication_suggestions = []

    account = Account.objects.get(id=id)
    contact_ids = Follow.objects.filter(follower=id).values_list('following', flat=True)

    if contact_ids.count() == 0:
        suggestions_data = Account.objects.exclude(id=id).annotate(num_following=Count('following')).order_by('-num_following')[:5]
        contact_suggestions = ContactsSerializer(suggestions_data, many=True).data

        publications_data = Post.objects.filter(Q(account__id__in=contact_ids))
        publications = ContactsSerializer(publications_data, many=True).data

    else:
        contacts_data = Account.objects.filter(locality=account.locality)[:5]
        contacts = ContactsSerializer(contacts_data, many=True).data

        last_week = timezone.now() - timezone.timedelta(days=7)

        publication_suggestions_data = Post.objects.filter(post_date__gte=last_week).annotate(total_likes=Sum('likes')).order_by('-total_likes')
        publication_suggestions = ContactsSerializer(publication_suggestions_data, many=True).data

    return JsonResponse({
        "contacts": contacts,
        "contact_suggestions": contact_suggestions,
        "publications": publications,
        "publication_suggestions": publication_suggestions,
    })