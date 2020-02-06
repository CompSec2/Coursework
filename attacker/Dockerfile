FROM python:3.8.1-alpine3.11

ADD requirements.py .
RUN pip install -r /requirements.py

ADD attack.py .

RUN touch hold.txt
CMD echo "plotting" && tail -f hold.txt