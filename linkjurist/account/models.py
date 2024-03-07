import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from tags.models import Tag


def account_directory_path(instance, image):
    return f'imgs/{instance.id}/{image}'


class Account(models.Model):
    name = models.CharField(unique=True, max_length=128)    
    description = models.TextField()
    slogan = models.CharField(null=True, blank=True, max_length=128)
    email = models.EmailField(blank=True)
    web = models.CharField(max_length=256, blank=True)
    address = models.CharField(max_length=256, blank=True)
    cp = models.CharField(max_length=256, blank=True)
    locality = models.CharField(max_length=256, blank=True)
    country = models.CharField(max_length=256, blank=True)
    phonenumber = models.CharField(max_length=256, blank=True)
    image = models.URLField(null=False, default="")

    def __str__(self):
        return str(self.name)
    

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    is_manager = models.BooleanField(default=False)
    image = models.URLField(null=False, default="")

    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, through='UserTag', related_name='users')

    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'password']

    def __str__(self):
        return self.email
    

class UserTag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.firstname} - {self.tag.name}"
    

class Follow(models.Model):
    follower = models.ForeignKey(Account, related_name='followers', on_delete=models.CASCADE)
    following = models.ForeignKey(Account, related_name='following', on_delete=models.CASCADE)
    created_at = models.DateField(null=False, auto_now=False, auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')


class Review(models.Model):
    posted_by = models.ForeignKey(User, related_name='posted_by', on_delete=models.CASCADE)
    posted_to = models.ForeignKey(Account, related_name='posted_to', on_delete=models.CASCADE)
    rating = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('posted_by', 'posted_to')
