from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200,default="username")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

class Category(models.Model):
    name = models.CharField(max_length=200)

class Author(models.Model):
    name = models.CharField(max_length=200)

class Books(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    file = models.FileField(upload_to="books/",blank=True,null=True)
    
