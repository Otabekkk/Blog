from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now

class Post(models.Model):
    title = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(max_length = 200, unique = True, blank = True)
    published_at = models.DateField(default = now)
    created_at = models.DateTimeField(auto_now_add = True)
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
