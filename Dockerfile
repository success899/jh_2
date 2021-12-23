FROM python:3.9.0

WORKDIR /home/

RUN echo 'asdhasdh'

RUN git clone https://github.com/success899/jh_2.git

WORKDIR /home/jh_2/

RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=jh_2.settings.deploy && python manage.py migrate --settings=jh_2.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=jh_2.settings.deploy jh_2.wsgi --bind 0.0.0.0:8000"]