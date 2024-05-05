FROM python:3.12

RUN pip install --upgrade pip
RUN pip install django gunicorn

WORKDIR /app

COPY . /app
RUN chmod +x /app/entrypoint.sh
RUN python manage.py collectstatic --noinput
VOLUME /app/db/

EXPOSE 8000
ENTRYPOINT ["/app/entrypoint.sh"]
