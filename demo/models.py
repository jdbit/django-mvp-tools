from django.db import models
from django.urls import reverse
from core.models import Page
from core.models import User
from taggit.managers import TaggableManager


class Post(Page):
    created_by = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    thumb = models.ImageField(default='default-thumb.jpg')
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-view', kwargs={'slug': self.slug})


def check_comments_input_allowed(obj):
    return True
