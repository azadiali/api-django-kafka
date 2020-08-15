# API service with Kafka

docker-compose -f api-django-kafka.yml up -d

=====================================\n

data input (with POST method) example:   

{

    "first_name": "example",
    "last_name": "example",
    "email": "info@example.com"

}



data gathering example:

[IP]:8000/?name=example



