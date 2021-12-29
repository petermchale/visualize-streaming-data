## Visualize the geographic location of tweets in real time using kafka

Stream geo-tagged tweets via Kafka to a web-app visualization using Flask streaming and HTML5 Server-Sent Events.

Based upon: https://medium.com/an-idea/real-time-twitter-map-with-javascript-python-and-kafka-a95d6bf34b92

```
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties

bin/kafka-topics.sh --create --partitions 3 --replication-factor 1 --topic twitter --bootstrap-server localhost:9092
bin/kafka-topics.sh --describe --topic twitter --bootstrap-server localhost:9092
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic twitter

python stream.py
python app.py
```