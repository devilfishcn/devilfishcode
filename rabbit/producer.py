# -*- coding: utf-8 -*-

import pika
import time

# 建立一个实例
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost',5672)  # 默认端口5672，可不写
    )
# 声明一个管道，在管道里发消息
channel = connection.channel()
# 在管道里声明queue
channel.queue_declare(queue='hello2',durable=True)
# RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.

i = 0
while(i<10):
    i+=1
    msg='hello world '+str(i)
    channel.basic_publish(exchange='',
                          routing_key='hello2',  # queue名字
                          #body='Hello World!',
                          body=msg,
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                              ))  # 消息内容
    time.sleep(2)
    print "send msg: %s" % msg
connection.close()  # 队列关闭