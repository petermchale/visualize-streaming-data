from pykafka import KafkaClient

def get_kafka_topic():
    client = KafkaClient(hosts='127.0.0.1:9092')
    topic = client.topics['twitter']
    return topic
