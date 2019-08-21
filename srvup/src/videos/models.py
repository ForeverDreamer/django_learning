from django.db import models


class Video(models.Model):
    embed_code = models.TextField()

    def __str__(self):
        return self.embed_code
