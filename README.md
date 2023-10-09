# Apache Kafka Real-Time Streaming Example
This repository contains a simple example of how to use Apache Kafka for real-time streaming in Python. The example includes a Kafka producer that sends messages to a Kafka topic, and a Kafka consumer that receives and prints these messages.


Description-

Apache Kafka is a distributed streaming platform that is widely used for real-time data streaming. It provides a publish-subscribe model for real-time data feeds. This example demonstrates how to create a Kafka producer and consumer in Python, which allows for real-time data processing and analysis.


Requirements-

Python 3.x
confluent-kafka library
You can install the confluent-kafka library using pip:

pip install confluent-kafka


Usage-

Run the producer script to send messages to a Kafka topic:

python kproducer.py

Run the consumer script to receive and print messages from the Kafka topic:

python kconsumer.py