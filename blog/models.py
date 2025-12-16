from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status= self.model.Status.PUBLISHED)

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    body = RichTextField()
    slug = models.SlugField(max_length=200)
    image = CloudinaryField('image',folder ='friends_of_fuo/blog', blank=True, null=True)
    published_date =models.DateTimeField(default=timezone.now) 
    status = models.CharField(max_length=2, choices= Status.choices, default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()
    class Meta:
        ordering = ['-published_date']
    def __str__(self):
        return self.title
        
