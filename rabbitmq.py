#!/usr/bin/python3
try:
    import pika
    from pika.exceptions import UnroutableError, NackError
    import configparser
    import json
except Exception as err:
    print('some Python modules are missing {}'.format_map(err))

try:
    parser = configparser.ConfigParser()
    parser.read('config.ini')
except configparser.ParsingError as err:
    print("Config not Found {}".format_map(err))

pika_server = parser.get('AMQP', 'server')
pika_queue = parser.get('AMQP', 'queue')
pika_exchange = parser.get('AMQP', 'exchange')
pika_user = parser.get('AMQP', 'user')
pkia_pass = parser.get('AMQP', 'password')
creds = pika.PlainCredentials(pika_user, pkia_pass)


class RabbitMq(object):
    def __init__(self, queue=pika_queue):
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=pika_server, credentials=creds))
        self._channel = self._connection.channel()
        self.queue = queue
        self._channel.queue_declare(queue=self.queue, durable=True)
        self._channel.exchange_declare(exchange=pika_exchange, exchange_type='direct', passive=False, durable=True,
                                       auto_delete=False, internal=False)

    def publish(self, payload={}):
        try:
            self._channel.basic_publish(exchange=pika_exchange, routing_key=pika_queue, body=json.dumps(payload))
            self._connection.close()
        except (UnroutableError, NackError) as e:
            print('Rabbit MQ Error', e)
