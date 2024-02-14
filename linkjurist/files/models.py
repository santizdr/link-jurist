from django.db import models
from account.models import Account, User
from tags.models import Tag


def user_directory_path(instance, filename):
    return f'uploads/{instance.account.id}/{filename}'

class File(models.Model):
    title = models.CharField(max_length=128)
    file = models.FileField(null=False, upload_to=user_directory_path)
    description = models.TextField(blank=True)
    post_date = models.DateField(null=False, auto_now=False, auto_now_add=True)
    downloads = models.PositiveIntegerField(null=False, default=0)
    price = models.DecimalField(null=False, max_digits=5, decimal_places=2)

    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return str(self.name)