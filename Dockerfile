FROM python:3.13
RUN mkdir /var/www
WORKDIR /var/www
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY sample/*.py ./sample/
COPY uwsgi.ini ./
CMD ["uwsgi", "--ini", "/var/www/uwsgi.ini"]
