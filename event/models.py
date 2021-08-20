from django.db import models
from django.utils import timezone
# Create your models here.
from django.db import models


# import qrcode
# from io import BytesIO
# from django.core.files import File
# from PIL import Image, ImageDraw


class Join(models.Model):
  name                = models.CharField(max_length=100)
  email               = models.EmailField()
  year                = models.CharField(max_length=100)
  attend              = models.CharField(max_length=100)
  note                = models.TextField(null=True, blank=True)
  date                = models.TimeField(auto_now_add=True)
    


class Image(models.Model):
  id                  = models.AutoField(primary_key=True)
  year                = models.CharField(max_length=100)
  image               = models.ImageField(upload_to='images/', null=True, blank=True)
  status              = models.BooleanField(default=False)


class Cooperate(models.Model):
  name                = models.CharField(max_length=100)
  image               = models.ImageField(upload_to='company/')


  def __str__(self):
    return self.name


class Activity(models.Model):
  name                = models.CharField(max_length=100)
  image               = models.ImageField(upload_to='activity/')
  status              = models.BooleanField(default=True)

  def __str__(self):
    return self.name


class MailAdmin(models.Model):
  id                  = models.AutoField(primary_key=True)
  name                = models.CharField(max_length=100)
  email               = models.EmailField()

  def __str__(self):
    return self.name


class Title(models.Model):
  title               = models.CharField(max_length=1000)


  def __str__(self):
    return self.title

class Link_QRCode(models.Model):
  link                = models.CharField(max_length=300)

  def __str__(self):
    return self.link