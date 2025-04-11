from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(
        max_length=256,
        blank=False,
        null=False,
    )
    text = models.TextField(
        blank=False,
        null=False,
    )
    pub_data = models.DateTimeField(
        blank=False,
        null=False,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    location = models.ForeignKey(
        "Location",
        on_delete=models.SET_NULL,
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        blank=False,
        null=False,
    )
    is_published = models.BooleanField(
        default=True,
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )


class Category(models.Model):
    title = models.CharField(
        max_length=256,
        blank=False,
        null=False,
    )
    description = models.TextField(
        blank=False,
        null=False,
    )
    slug = models.SlugField(
        blank=False,
        null=False,
    )
    is_published = models.BooleanField(
        default=True,
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )


class Location(models.Model):
    name = models.CharField(
        max_length=256,
        blank=False,
        null=False,
    )
    is_published = models.BooleanField(
        default=True,
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )
