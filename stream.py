import tweepy
import credentials
import json
from colorize import print_json
from utils import get_kafka_topic
import time

class Stream(tweepy.Stream):
    def on_data(self, data):
        message = json.loads(data)
        if message['place'] is not None:
            print('*************')
            print_json(message)
            print('*************')
            kafka_producer.produce(data)
            time.sleep(1)
        return True

    def on_error(self, status):
        print('on_error')
        print(status)

def stream_to_kafka(): 
    stream = Stream(
        credentials.API_KEY,
        credentials.API_SECRET_KEY,
        credentials.ACCESS_TOKEN,
        credentials.ACCESS_TOKEN_SECRET
    )
    print('twitter_stream created')
    stream.filter(locations=[-180,-90,180,90])

def get_kafka_producer(): 
    topic = get_kafka_topic()
    producer = topic.get_sync_producer()
    return producer

if __name__ == "__main__":
    kafka_producer = get_kafka_producer()
    stream_to_kafka()
