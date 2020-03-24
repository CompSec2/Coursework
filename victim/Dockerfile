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

RUN apt-get update && apt-get install apache2 libapache2-mod-wsgi-py3 && sudo a2enmod wsgi

RUN mkdir -p victim.com/logs && sudo chown -R www-data:www-data victim.com
RUN /etc/init.d/apache2 reload

EXPOSE 5000

CMD ["/usr/local/bin/python", "app.py"]
