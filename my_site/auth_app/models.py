from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """
    Менеджер для создания кастомных пользователей
    """
    def create_user(self, username: str, password: str):
        """
        Создает обычного пользователя

        Args:
            username: str
            password: str

        Returns:
            user object

        """
        if username is None:
            raise TypeError('Username обязателен')
        elif password is None:
            raise TypeError('Пароль обязателен')

        user = self.model(username=username)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username: str, password: str):
        """
        Создает суперпользователя на основе функции create_user

        Args:
            username: str
            password: str

        Returns:
            user object
        """
        user = self.create_user(username=username, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Модель пользователя. Поле USERNAME_FIELD должно быть явно указано
    """
    username = models.CharField(db_index=True, max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "username"
    objects = UserManager()

    def __str__(self):
        return self.username

