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
- добавление модели сообщества
- добавление связи m2m блога и сообщества
- добавление o2m связь автора и блога
- проверка работы сигналов
- по сигналу вносятся изменения в статус блога
- статус каждого блога пользователя отображен в профиле

### TODO
- автоматическое создание групп (с правами)
- автоматическое создание пользователей (админа, модератора, несколько пользователей)
- упаковать в докер (опционально)
- автозаполнение блогов random значениями (опционально)
- проверить работу уведомления на почту пользоватей о модерации (опционально)

### Issues
- если модерируемая модель свяазана отношениями m2m, то в админке они не отобразятся
- предупреждение с сохранением времени TZ (?)


## Запуск проекта
```sh
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
