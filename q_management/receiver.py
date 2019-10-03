import pika
import json
from pymongo import MongoClient
import db_config as db

conn = MongoClient()
database = conn["locale"]
col = database["rides"]


connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.queue_declare(queue="hello")


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    db.insert_record(json.loads(body.decode("utf-8")))


channel.basic_consume(queue="hello", auto_ack=True, on_message_callback=callback)

print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
