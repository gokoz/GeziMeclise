from django.db import models
from django_facebook.models import FacebookModel
from django.contrib.auth.models import AbstractUser, UserManager
from taggit.managers import TaggableManager


class GeziUser(AbstractUser, FacebookModel):
    supports = models.ManyToManyField('self', blank=True, related_name='supporters')
    causes = models.TextField(blank=True, null=True)
    tags = TaggableManager(blank=True)

    objects = UserManager()
