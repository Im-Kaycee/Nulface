from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('index')

class Posts(models.Model):
    title = models.CharField(max_length=255)  # For the blog post title
    #content = models.TextField() #content
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateField(default=datetime.date.today) #date posted
    category = models.CharField(max_length=255)#category
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.title} {self.date_posted}"
    
    def get_absolute_url(self):
        return reverse('post', args=(str(self.id)))