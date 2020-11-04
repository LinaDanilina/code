FROM python:3.8.3-alpine
#RUN mkdir /code
WORKDIR /code
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
#ADD requirements.txt /code/
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
RUN pip install gunicorn
COPY requirements.txt  /code/
RUN pip install -r requirements.txt
COPY entrypoint.sh /code/
RUN chmod +x ./entrypoint.sh
COPY . .
ENTRYPOINT ["./entrypoint.sh"]