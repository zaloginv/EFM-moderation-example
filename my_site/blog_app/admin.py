from django.contrib import admin
from moderation.admin import ModerationAdmin
from .models import Blog, Community


@admin.register(Blog)
class BlogAdmin(ModerationAdmin):
    """Обычные админ настройки"""
    pass


@admin.register(Community)
class BlogAdmin(admin.ModelAdmin):
    """Обычные админ настройки"""
    pass
