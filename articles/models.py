from django.conf import settings
from django.db import models

from taggit.managers import TaggableManager


class Article(models.Model):
    author = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='blog_article'
    )
    title = models.CharField(max_length=255)
    title_image = models.ImageField(upload_to='title_image/')
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    class Meta:
        app_label = 'articles'
        ordering = ('-created', )
        verbose_name = 'Artykuł'
        verbose_name_plural = 'Artykułyt'

    def __str__(self):
        return self.title
