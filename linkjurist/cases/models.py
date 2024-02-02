from django.db import models
from datetime import date
from account.models import Account

# Create your models here.

class Case(models.Model):
    CASE_TYPES = (("OFFER", "Oferta"), ("DEMAND", "Demanda"))
    
    title = models.CharField(null=False, max_length=256)    
    description = models.TextField(null=False)
    type = models.CharField(null=False, choices=CASE_TYPES)
    post_date = models.DateField(null=False, auto_now=False, auto_now_add=True)
    expiry_date = models.DateField(null=False, auto_now=False, auto_now_add=False)
    applications = models.PositiveIntegerField(null=False, default=0)
    visualizations = models.PositiveIntegerField(null=False, default=0)
    percent = models.DecimalField(null=False, max_digits=5, decimal_places=2)

    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.title)