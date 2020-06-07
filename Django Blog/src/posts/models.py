from django.db import models
from django.core.files.storage import FileSystemStorage
from datetime import date
from django.utils.timezone import now
# Create your models here.
class Post(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    publishedAt = models.DateField(default= now)

    def __str__(self):
        return self.title
    