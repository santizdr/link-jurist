from django.db import models
from account.models import Account, User
from tags.models import Tag


class Post(models.Model):    
    content = models.TextField(null=False, max_length=512)    
    post_date = models.DateField(null=False, auto_now=False, auto_now_add=True)
    visualizations = models.PositiveIntegerField(null=False, default=0)

    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    tags = models.ManyToManyField(Tag, through='PostTag', related_name='posts')

    def __str__(self):
        return str("Publicado por: " + self.posted_by)
    

class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post.title} - {self.tag.name}"
    

class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} {self.tag.lastname} le gusta tu publicación"
