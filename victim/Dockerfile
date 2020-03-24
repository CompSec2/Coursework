FROM python:3.8.1-alpine3.11

RUN apk update
RUN apk add tcpdump

ADD requirements.txt .

RUN apk add gcc
RUN apk add libc-dev
RUN apk add linux-headers

RUN pip install -r /requirements.txt

RUN pip install uwsgi==2.0.14
RUN apk add uwsgi-python3

WORKDIR /var/www
ADD app.py .
ADD templates templates
ADD static static
ADD sniff.py .
ADD victim.wsgi .
ADD victim.com.conf /etc/apache2/sites-available/

RUN apk update && apk add apache2-dev
RUN pip install mod_wsgi
RUN a2enmod wsgi

RUN mkdir -p /var/www/victim.com/logs && chown -R 771 /var/www/victim.com

EXPOSE 5000

CMD ["/usr/local/bin/python", "app.py"]
