from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.db.models import Count

from courses.utils import create_slug
from videos.models import Video


class CategoryQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all(
        ).active().annotate(
            courses_length=Count("secondary_category", distinct=True)
        ).prefetch_related('primary_category', 'secondary_category')

        # qs = Category.objects.all()
        # obj = qs.first()
        # courses = obj.course_set.all() # models unleashed


class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    video = models.ForeignKey(Video, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CategoryManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("categories:detail", kwargs={"slug": self.slug})


def pre_save_category_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_category_receiver, sender=Category)
