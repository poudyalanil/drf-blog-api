from django.db import models

class Category(models.Model):
    category= models.CharField(max_length=255,default=None, blank=False,verbose_name="Category Name")
    date_created = models.DateTimeField(auto_now=True)
    creator = models.CharField(max_length=255,default=None,blank=False,verbose_name="Creator")


class Tag(models.Model):
    tag = models.CharField(max_length=255,default=None,blank=False,verbose_name="Tag Name")
    date_created = models.DateTimeField(auto_now=True)
    creator = models.CharField(max_length=255,default=None,blank=False,verbose_name="Creator")
