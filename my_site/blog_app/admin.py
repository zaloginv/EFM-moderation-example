from django.contrib import admin
from moderation.admin import ModerationAdmin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(ModerationAdmin):
    """Обычные админ настройки"""
    pass
