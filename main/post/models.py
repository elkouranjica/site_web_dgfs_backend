from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager

from main.abstract.models import AbstractModel


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404


def post_image_directory_path(instance, filename):
    return "post_{0}/{1}".format(instance.public_id, filename)


class Post(AbstractModel):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Brouillon'
        PUBLISHED = 'PB', 'Publié'

    title = models.CharField(max_length=250)
    summary = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    tags = TaggableManager()
    image = models.ImageField(upload_to=post_image_directory_path, blank=True, null=True)

    def __str__(self):
        return self.title

    objects = models.Manager()  # objects manager par défaut
    published = PublishedManager()  # objects manager customizé pour les articles publié

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]
