FROM python:3.10.14-alpine

ENV TELEGRAM_TOKEN _
ENV TELEGRAM_CHATID _

RUN mkdir /config

WORKDIR /app
COPY requirements.txt .
COPY main.py .
COPY dbinit.py .

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]