FROM python:3.10
WORKDIR app
COPY . .
RUN python -m pip install --upgrade pip && pip install -r my_site/requirements.txt