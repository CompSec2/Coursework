FROM python:3.8.2-buster

RUN apt-get update \
 && apt-get install -y tcpdump libapache2-mod-wsgi-py3 apache2 apache2-dev \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/victim.com

ADD requirements.txt .
RUN python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

ADD app/ .
ADD sniff.py .
ADD app/victim.com.conf /etc/apache2/sites-available/victim.com.conf

RUN mkdir -p /var/www/victim.com/logs && chown -R 771 /var/www/victim.com

RUN a2dissite 000-default.conf && a2enmod wsgi && a2ensite victim.com

EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]