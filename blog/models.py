from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=225, unique=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=150, blank=True)
    date_modified = models.DateTimeField(auto_now=True)
    text = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=False, null=True)

    def published(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.title