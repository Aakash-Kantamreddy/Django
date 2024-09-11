from django.db import models
from datetime import datetime

# Create your models here.

class data(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateField(default = datetime.now(),blank=True)
    is_published = models.BooleanField(default=False)
    description = models.TextField()
    video = models.FileField(upload_to="videos/",null=True)
    


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'data'
        verbose_name_plural = 'datas'
