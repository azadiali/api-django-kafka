FROM python:3.7.8-slim-stretch
RUN apt update -y
RUN apt-get install build-essential -y
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip3 install --no-cache-dir django
RUN pip3 install --no-cache-dir kafka-python
RUN pip3 install --no-cache-dir uwsgi
EXPOSE 8000
COPY *.ini /app
COPY entrypoint.sh /app
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh" , "api-django-kafka"]
