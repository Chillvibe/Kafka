from confluent_kafka import Producer

# Create a Kafka producer instance
p = Producer({'bootstrap.servers': 'localhost:9092'})

# Define a callback function to handle delivery reports
def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))  # If the message fails to deliver, print an error
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))  # If the message is delivered successfully, print its topic and partition

# Produce some data to a Kafka topic
for data in some_data_source:
    p.produce('mytopic', data.encode('utf-8'), callback=delivery_report)  # Encode the data as bytes and send it to the topic 'mytopic'. The delivery_report callback function will be triggered when the message is delivered or fails to deliver.

# Wait for any outstanding messages to be delivered and delivery reports to be received
p.flush()
