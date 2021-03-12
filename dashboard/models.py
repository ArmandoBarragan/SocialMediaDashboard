from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CommonModel(models.Model):
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True

class User(AbstractUser):
    email = models.EmailField(max_length=50)
    business_name = models.CharField(max_length=30)
