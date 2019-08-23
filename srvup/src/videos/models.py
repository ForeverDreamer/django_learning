from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


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


def pre_save_video_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


pre_save.connect(pre_save_video_receiver, sender=Video)
