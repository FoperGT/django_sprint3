from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=256,
        blank=False,
        null=False,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=False,
        null=False,
    )
    slug = models.SlugField(
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.',
        unique=True,
        blank=False,
        null=False,
    )
    is_published = models.BooleanField(
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.',
        default=True,
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(
        verbose_name='Добавлено',
        auto_now_add=True,
        blank=False,
        null=False,
    )
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(models.Model):
    name = models.CharField(
        verbose_name='Название места',
        max_length=256,
        blank=False,
        null=False,
    )
    is_published = models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(
        verbose_name='Добавлено',
        auto_now_add=True,
        blank=False,
        null=False,
    )
    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Post(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=256,
        blank=False,
        null=False,
    )
    text = models.TextField(
        verbose_name='Текст',
        blank=False,
        null=False,
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем — можно делать отложенные публикации.',
        blank=False,
        null=False,
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор публикации',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    location = models.ForeignKey(
        Location,
        verbose_name='Местоположение',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE,
        blank=False,
        null=True,
    )
    is_published = models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(
        verbose_name='Добавлено',
        auto_now_add=True,
        blank=False,
        null=False,
    )
    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural='Публикации'
