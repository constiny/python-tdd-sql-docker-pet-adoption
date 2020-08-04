FROM python:3.8.5-buster

WORKDIR /usr/src/app

COPY . .

RUN apt update && apt install sqlite3