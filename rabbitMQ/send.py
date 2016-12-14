import pika

c = pika.PlainCredentials('me', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.31.180',credentials=c,virtual_host='new_one'))
channel=connection.channel()

channel.queue_declare(queue='user_me')
channel.basic_publish(exchange='',routing_key='user_me',body="hello me")

connection.close()