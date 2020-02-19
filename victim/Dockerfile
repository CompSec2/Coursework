FROM python:3.8.1-alpine3.11

ADD requirements.txt .
RUN pip install -r /requirements.txt

ADD app.py .
ADD templates
EXPOSE 5000

CMD ["/usr/local/bin/python", "app.py"]