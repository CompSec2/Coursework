FROM python:3.8.2-buster

ADD requirements.txt .
RUN pip install -r /requirements.txt

ADD attack.py .

RUN touch hold.txt
CMD echo "plotting" && tail -f hold.txt
