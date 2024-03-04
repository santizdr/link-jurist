from django.db import models
from account.models import Account
from tags.models import Tag


class Case(models.Model):
    CASE_TYPES = (("OFFER", "Oferta"), ("DEMAND", "Demanda"))
    
    title = models.CharField(null=False, max_length=256)    
    description = models.TextField(null=False)
    type = models.CharField(null=False, choices=CASE_TYPES)
    post_date = models.DateField(null=False, auto_now=False, auto_now_add=True)
    expiry_date = models.DateField(null=False, auto_now=False, auto_now_add=False)
    applications = models.PositiveIntegerField(null=False, default=0)

    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    tags = models.ManyToManyField(Tag, through='CaseTag', related_name='cases')

    def __str__(self):
        return str(self.title)
    

class CaseTag(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.case.title} - {self.tag.name}"
    

class Apply(models.Model):
    STATUSES = (("PENDING", "Pendiente"), ("ACCEPTED", "Aceptada"), ("DENIED", "Rechazada"))

    status = models.CharField(null=False, choices=STATUSES, default="PENDING")
    applicant = models.ForeignKey(Account, related_name='applicant', on_delete=models.CASCADE)

    case = models.ForeignKey(Case, on_delete=models.CASCADE, null=False)
