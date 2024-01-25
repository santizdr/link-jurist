from datetime import date
from django.db import models

from account.models import Account, User

# Create your models here.

class File(models.Model):

    name = models.CharField(null=False, max_length=256)    
    description = models.TextField()
    post_date = models.DateField(null=False, auto_now=False, auto_now_add=date.today())
    downloads = models.PositiveIntegerField(null=False, default=0)
    price = models.DecimalField(null=False, max_digits=5, decimal_places=2)

    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.name)