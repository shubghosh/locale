import pika


def start_queuing(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="hello")

    i = channel.basic_publish(exchange="", routing_key="hello", body=str(data))
    print("Sent Request")
    print(i)
    connection.close()
