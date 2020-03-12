FROM python:3.8.1-alpine3.11

RUN apk update
RUN apk add tcpdump

ADD requirements.txt .
RUN pip install -r /requirements.txt

ADD app.py .
ADD templates templates
ADD static static
ADD sniff.py .

EXPOSE 5000

CMD ["/usr/local/bin/python", "app.py"]
