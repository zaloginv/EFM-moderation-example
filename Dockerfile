FROM python:3.10
COPY ./my_site ./my_site
RUN python -m pip install --upgrade pip && pip install -r my_site/requirements.txt
RUN cd my_site \
    && python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py fill_db
CMD ["python", "manage.py", "runserver"]