from confluent_kafka import Consumer, KafkaException

# Create a Kafka consumer instance
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
}

c = Consumer(conf)

# Subscribe to a Kafka topic
c.subscribe(['mytopic'])

# Continuously poll for new messages
while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        raise KafkaException(msg.error())  # If there's an error with the message, raise an exception
    else:
        print('Received message: {}'.format(msg.value().decode('utf-8')))  # If the message is received successfully, print its value

# Close the consumer to free up resources
c.close()
