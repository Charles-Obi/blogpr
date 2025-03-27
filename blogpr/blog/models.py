from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date_created = models.DateField()

    def __str__(self):
        return self.title
    
class CustomUser(models.Model):
    ROLES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=ROLES, default='user')

    def __str__(self):
        return self.user.username
