from django.conf import settings
from django.db import models


class Blog(models.Model):
    """
    Модель блога. Может быть в активном или неактивном состоянии
    """

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    body = models.CharField(max_length=1000, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.title
