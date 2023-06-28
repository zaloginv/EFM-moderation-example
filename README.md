## Описание
Проект разделен на два приложения:
- авторизация
- блоги

### Done
- регистрация пользователя
- login, logout
- просмотр профиля пользователя
- создание блога
- просмотр списка блогов
- просмотр каждого блога
- редактирование блога для запроса на модерацию
- добавление и настройка django-moderation

### TODO
- исправление ошибки с TZ
- настройка сигналов для оповещения пользователей
- автоматическое создание групп
- автоматическое создание пользователей (админа, модератора, несколько пользователей)
- упаковать в докер
- автозаполнение блогов random значениями (опционально)


## Запуск проекта
```sh
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
