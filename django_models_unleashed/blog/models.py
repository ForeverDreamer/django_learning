from datetime import timedelta, datetime, date

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.encoding import smart_text
from django.utils import timezone
from django.utils.text import slugify
from django.utils.timesince import timesince

from .validators import validate_justin, validate_author_email

PUBLISH_CHOICES = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private'),
)


class PostModelQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def post_title_items(self, value):
        return self.filter(title_icontains=value)


class PostModelManager(models.Manager):
    def get_queryset(self):
        return PostModelQuerySet(self.model, using=self._db)

    def all(self, *args, **kwargs):
        # qs = super(PostModelManager, self).all(*args, **kwargs).active()  # .filter(active=True)
        # print(qs)
        qs = self.get_queryset().active()
        return qs

    def get_timeframe(self, date1, date2):
        qs = self.get_queryset()
        qs_time_1 = qs.filter(publish_date_gte=date1)
        qs_time_2 = qs_time_1.filter(publish_date_lt=date2)
        return qs_time_2


class PostModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    active = models.BooleanField(default=True)
    title = models.CharField(
        max_length=240,
        verbose_name='Post title',
        unique=True,
        error_messages={
            'unique': "This title is not unique, please try again."
        },
        help_text="Must be a unique title."
    )
    slug = models.SlugField(null=True, blank=True, editable=False)
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    # author_email = models.CharField(max_length=240, validators=[validate_author_email, validate_justin], null=True,
    #                                 blank=True)
    author_email = models.EmailField(max_length=240, validators=[validate_justin], null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = PostModelManager()
    # other = PostModelManager()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        # unique_together = ['title', 'slug']

    def __str__(self):
        return smart_text(self.title)

    # def random_method(self, abc, edb, title, keyword1=None, keyword2=None):
    #     print(title)
    #     print(keyword1)

    def save(self, *args, **kwargs):
        # if not self.slug and self.title:
        #     self.slug = slugify(self.title)
        # 尽量使用signals的pre_save, post_save，避免重写此父类方法
        super(PostModel, self).save(*args, **kwargs)

    @property
    def age(self):
        if self.publish == 'publish':
            now = datetime.now()
            publish_time = datetime.combine(self.publish_date, datetime.now().min.time())
            try:
                difference = now - publish_time
            except:
                return 'Unknown'
            if difference <= timedelta(minutes=1):
                return 'Just now'
            return '{time} ago'.format(time=timesince(publish_time).split(', ')[0])
        return 'Not published'
        # return '{t} ago'.format(t=timesince(self.publish_date))


def postmodel_pre_save_receiver(sender, instance, *args, **kwargs):
    print('Before save')
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)


pre_save.connect(postmodel_pre_save_receiver, sender=PostModel)


def postmodel_post_save_receiver(sender, instance, created, *args, **kwargs):
    print('After save')
    print(created)
    if created:
        if not instance.slug and instance.title:
            instance.slug = slugify(instance.title)
            instance.save()


post_save.connect(postmodel_post_save_receiver, sender=PostModel)
