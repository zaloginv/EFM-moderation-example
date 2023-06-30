from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from blog_app.models import Community


class Command(BaseCommand):
    def handle(self, **options):
        """
        Создание группы модераторов с разрешением на просмотр
        и изменение модерируемого объекта

        Создание сообществ

        Заполнение базы данных пользователями:
            admin (есть все права)
            moder (может модерировать блоги)
            vasyan (пользуется сайтом)

        У каждого из них password = username
        """

        group = Group.objects.create(name='moders')

        moder_perm_view = Permission.objects.get(codename='view_moderatedobject')
        moder_perm_change = Permission.objects.get(codename='change_moderatedobject')

        group.permissions.add(moder_perm_view)
        group.permissions.add(moder_perm_change)

        Community.objects.create(name='Спорт', description='Спортивное сообщество')
        Community.objects.create(name='Политика', description='Политическое сообщество')

        User = get_user_model()

        User.objects.create_superuser('admin', 'admin')
        User.objects.create_user('vasyan', 'vasyan')
        User.objects.create_user('moder', 'moder')

        moder = User.objects.get(username='moder')
        moder.is_staff = True
        moder.save()
        moder.groups.add(group)
