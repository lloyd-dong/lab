import pika
import sys
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.31.180'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',type='direct')
result=channel.queue_declare(exclusive=True)
queue_name=result.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage %s [info] [warning] [error] \n" % sys.argv[0])
    sys.exit(1)
	
for severity in severities:
    channel.queue_bind(exchange='direct_logs',queue=queue_name,routing_key=severity)

def callback(ch, method, properties, body):
    print(" [x] Received %r:%r" % (method.routing_key, body))
    time.sleep(3)
    print(" [x] done")
	

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()