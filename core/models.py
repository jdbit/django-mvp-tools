from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import make_unique_slug


class User(AbstractUser):
    pass


class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True,
                            blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            new_slug = make_unique_slug(Page, self.title)
            self.slug = new_slug.replace("/", "-")
        super(Page, self).save(*args, **kwargs)


class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    message = models.TextField(max_length=2048, blank=True, null=True)
    createdon = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/contact/'
