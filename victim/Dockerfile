FROM python:3.8.1-alpine3.11

RUN apk update
RUN apk add tcpdump

ADD requirements.txt .
RUN pip install -r /requirements.txt

WORKDIR /var/www
ADD app.py .
ADD templates templates
ADD static static
ADD sniff.py .
ADD victim.wsgi

RUN apt-get install apache2
RUN apt-get install libapache2-mod-wsgi-py3
RUN a2enmod wsgi
RUN apt-get install python-pip
RUN pip install virtualenv
RUN virtualenv /victim/venv
source victim/venv/bin/activate
RUN pip install Flask

RUN mkdir -p victim.com/logs
RUN chown -R www-data:www-data victim.com

EXPOSE 5000

CMD ["/usr/local/bin/python", "app.py"]
