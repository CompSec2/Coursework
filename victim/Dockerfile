FROM python:3.8.1-alpine3.11

ADD requirements.py .
RUN pip install -r /requirements.py

ADD app.py .
EXPOSE 5000

CMD ["/usr/local/bin/python", "app.py"]