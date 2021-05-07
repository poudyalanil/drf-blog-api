from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import  slugify

class Category(models.Model):
    category= models.CharField(max_length=255,default=None, blank=False,verbose_name="Category Name")
    date_created = models.DateTimeField(auto_now=True)
    creator = models.CharField(max_length=255,default=None,blank=False,verbose_name="Creator")

    def __str__(self):
        return self.category

class Tag(models.Model):
    tag = models.CharField(max_length=255,default=None,blank=False,verbose_name="Tag Name")
    date_created = models.DateTimeField(auto_now=True)
    creator = models.CharField(max_length=255,default=None,blank=False,verbose_name="Creator")

    def __str__(self):
        return self.tag

class Blog(models.Model):
    date_updated= models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag)
    category = models.ManyToManyField(Category)
    title  = models.CharField(max_length=255,default=None,blank=False,null=False)
    content = models.TextField(blank=False,default=None)
    author = models.CharField(max_length=255,default="Anonymus",blank=True,null=False)
    slug= models.SlugField(max_length=255,default=title,unique=True)
    feature_image = CloudinaryField(null=True,blank=True)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
            self.slug = slugify(self.title) # set the slug explicitly
            super(Blog, self).save(*args, **kwargs) # call Django's save()

# class Comment(models.Model):



