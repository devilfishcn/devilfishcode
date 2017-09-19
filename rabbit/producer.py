import pika

# ����һ��ʵ��
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost',5672)  # Ĭ�϶˿�5672���ɲ�д
    )
# ����һ���ܵ����ڹܵ��﷢��Ϣ
channel = connection.channel()
# �ڹܵ�������queue
channel.queue_declare(queue='hello')
# RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',  # queue����
                      body='Hello World!')  # ��Ϣ����
print(" [x] Sent 'Hello World!'")
connection.close()  # ���йر�