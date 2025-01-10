from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now

class Post(models.Model):
    title = models.CharField(max_length = 50)
