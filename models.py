from django.db import models
from django.contrib.auth.models import User
class student(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    profile_pic=models.ImageField(upload_to='profile_photo')

# Create your models here.
