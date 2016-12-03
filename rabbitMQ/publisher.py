import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.31.180'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',type='direct')

severity=sys.argv[1] if len(sys.argv) >1 else 'info'
message = ' '.join(sys.argv[2:]) or "info: publisher Hello"

channel.basic_publish(exchange='direct_logs',routing_key=severity,body=message)
print("[x] Send %r" % message)
connection.close()
