FROM python:3.11-alpine

LABEL authors="Nikolai Kochkin"

WORKDIR /opt/home-bot

ARG TG_TOKEN

ARG QBT_HOST
ARG QBT_PORT
ARG QBT_USER
ARG QBT_PASS

ARG SRV_HOST=0.0.0.0
ARG SRV_PORT=8000

EXPOSE $SRV_PORT

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python", "./bot/app.py"]