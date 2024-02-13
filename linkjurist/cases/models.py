from django.db import models
from datetime import date
from account.models import Account


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
    

class Apply(models.Model):
    STATUSES = (("PENDING", "Pendiente"), ("ACCEPTED", "Aceptada"), ("DENIED", "Rechazada"))

    status = models.CharField(null=False, choices=STATUSES, default="PENDING")
    applicant = models.ForeignKey(Account, related_name='applicant', on_delete=models.CASCADE)

    case = models.ForeignKey(Case, on_delete=models.CASCADE, null=False)
