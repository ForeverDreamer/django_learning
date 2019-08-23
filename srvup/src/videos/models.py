from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True)
    embed_code = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)  # time created
    updated = models.DateTimeField(auto_now=True)  # last saved

    def short_title(self):
        return self.title[:3]

    def __str__(self):
        return self.title
