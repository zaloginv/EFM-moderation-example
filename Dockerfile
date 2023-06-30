FROM python:3.10
WORKDIR my_site
COPY . ./
RUN python -m pip install --upgrade pip && pip install -r my_site/requirements.txt
RUN echo ls
#RUN python manage.py makemigrations \
#    && python manage.py migrate \
#    && python manage.py fill_db
#CMD ["python", "manage.py", "runserver"]