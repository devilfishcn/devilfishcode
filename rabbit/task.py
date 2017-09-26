# -*- coding: utf-8 -*-

import pika
import sys
import datetime
starttime = datetime.datetime.now()
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue')
#channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"

for i in range(10000):
    channel.basic_publish(exchange='',routing_key='task_queue',body=message)
    #channel.basic_publish(exchange='',routing_key='task_queue',body=message,properties=pika.BasicProperties(delivery_mode = 2,))
    print(" [x] Sent %r" % message)
connection.close()
endtime = datetime.datetime.now()
print (endtime - starttime).seconds