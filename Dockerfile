FROM python:3.5

#################

ENV PYTHONUNBUFFERED=1

RUN pip install urllib3
WORKDIR /usr/src/app
COPY . /usr/src/app

CMD ["python","./PotMHeartbeat.py"]
