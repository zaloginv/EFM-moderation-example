import moderation.models
from django.db import models
from moderation import signals
from moderation.db import ModeratedModel
from auth_app.models import User
from django.dispatch import receiver


class Community(models.Model):
    """
    Тематическое сообщество, где размещен(ы) блог(и)
    """
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=1000, verbose_name='Описание')

    def __str__(self):
        return self.name


class Blog(ModeratedModel):
    """
    Блог
    """
    on_check = 'on_check'
    rejected = 'rejected'
    approved = 'approved'

    STATUS_CHOICES = [
        (on_check, 'На проверке'),
        (rejected, 'Отклонено'),
        (approved, 'Одобрено')
    ]

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    body = models.CharField(max_length=1000, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    communities = models.ManyToManyField(Community, related_name='blogs')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=on_check)

    class Meta:
        ordering = ('created_at',)

    class Moderator:
        """
        Настройки модерации для текущей модели
        """
        notify_user = False  # по умолчанию True - отправляет уведомление на почту
        fields_exclude = ['status']

    def __str__(self):
        return self.title


@receiver(signal=signals.post_moderation)
def status_change(sender, instance, status, **kwargs):
    """
    Работает со встронным сигналом. Получаем модель, экземпляр модели и статус из модели-модератора.
    Независимо от прешедшего статуса, сохраняет изменения, что триггерит модель-модератор.
    Поэтому изменения нужно вносить и в неё тоже.
    Args:
        sender: model
        instance: model object
        status: bool
        **kwargs:
    """
    if status == 0:
        instance.status = Blog.rejected
    elif status == 1:
        instance.status = Blog.approved
    instance.save()
    moderated = moderation.models.ModeratedObject.objects.get_for_instance(instance)
    moderated.status = status
    moderated.save()
