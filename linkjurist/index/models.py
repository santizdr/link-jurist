from django.db import models
from account.models import Account, User
from datetime import date


class Post(models.Model):    
    content = models.TextField(null=False, max_length=512)    
    post_date = models.DateField(null=False, auto_now=False, auto_now_add=True)
    visualizations = models.PositiveIntegerField(null=False, default=0)
    likes = models.PositiveIntegerField(null=False, default=0)

    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str("Publicado por: " + self.posted_by)