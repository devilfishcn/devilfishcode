# -*- coding: utf-8 -*-

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672))
channel = connection.channel()
channel.exchange_declare(exchange='logs','fanout')

i = 0
while(i<10):
    i+=1
    msg='hello world '+str(i)
    channel.basic_publish(exchange='logs',routing_key='', body=msg)
    time.sleep(2)
    print "send msg: %s" % msg
connection.close()