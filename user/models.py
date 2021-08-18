from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class SomUser(AbstractUser):
    profileImage = models.ImageField(upload_to="mediaForm/",blank=True,null=True)
    introduce =  models.TextField()