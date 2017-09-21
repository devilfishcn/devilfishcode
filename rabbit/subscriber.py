# -*- coding: utf-8 -*-
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare('logs','fanout',False,True,False)
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
print("random queuename:", queue_name)
channel.queue_bind(exchange='logs',queue=queue_name)
def callback(ch, method, properties, body):
    print(" [x] %r" % body)
    time.sleep(3)
channel.basic_consume(callback,queue=queue_name,no_ack=True)
channel.start_consuming()