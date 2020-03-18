from django.db import models
from django.db.models import URLField


class Project(models.Model):
    title =  models.CharField(max_length=100)
    description =  models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url: URLField = models.URLField(blank=True)

    def __str__(self):
        return self.title


