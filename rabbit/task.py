# -*- coding: utf-8 -*-

import pika
import sys
import datetime
starttime = datetime.datetime.now()
connection = pika.BlockingConnection(pika.ConnectionParameters(host='47.94.206.52'))
channel = connection.channel()
channel.queue_declare(queue='task_queue')
#channel.queue_declare(queue='task_queue', durable=True)



for i in range(10000):
    message = ' '.join(sys.argv[1:]) or "Hello World!"
    message= message +str(i)
    channel.basic_publish(exchange='',routing_key='task_queue',body=message)
    #channel.basic_publish(exchange='',routing_key='task_queue',body=message,properties=pika.BasicProperties(delivery_mode = 2,))
    print(" [x] Sent %r" % message)
connection.close()
endtime = datetime.datetime.now()
print endtime - starttime

#测试结果：
#（1）1万，没有序列化，0:00:07.937000，0:01:01.568000，0:00:04.769000，0:00:01.747000，0:00:03.641000，0:00:02.691000