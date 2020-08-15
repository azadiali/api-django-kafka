from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from kafka import KafkaProducer
from api.models import Data
from kafka import KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic
from threading import Thread
import json





def run():
    print('listener started')

    consumer = KafkaConsumer('api_topic',bootstrap_servers=['kafka:9092'])
    for message in consumer:
        json = str(message).split('&')
        D = Data.objects.create(
            first_name = json[1],
            last_name = json[2],
            email = json[3],
        )
        print(json[1]) 
        print('write on db') 
def run2():
    admin_client = KafkaAdminClient(
    bootstrap_servers="kafka:9092", 
    )

    topic_list = []
    topic_list.append(NewTopic(name="api_topic", num_partitions=1, replication_factor=1))
    admin_client.create_topics(new_topics=topic_list, validate_only=False)
# def listener(request):
Thread(target=run).start()
    # return HttpResponse('started')
Thread(target=run2).start()


########GET&POST
def get_and_post(request):
    # POST
    if request.method == "POST":
       
        
        data = json.loads(request.body)
        data_to_send = f'&{data["first_name"]}&{data["last_name"]}&{data["email"]}&'



        producer = KafkaProducer(bootstrap_servers='kafka:9092')
        producer.send('api_topic', bytes(data_to_send, 'utf-8'))
        

        return HttpResponse('Writing data has been done!')
    
    # GET
    elif request.method == "GET":
        res = Data.objects.filter(first_name = request.GET.get('name')).last()
        js = {

            'first_name' : res.first_name,
            'last_name' : res.last_name,
            'email': res.email
            }
        return JsonResponse(js)
    
    else:
        return HttpResponse('method not allowed')
        



