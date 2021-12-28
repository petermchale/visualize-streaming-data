from flask import Flask, Response, render_template
import json
from utils import get_kafka_topic
from pykafka.common import OffsetType

app = Flask(__name__)

@app.route("/")
def index():
    return(render_template('index.html'))

# https://blog.miguelgrinberg.com/post/video-streaming-with-flask
# https://fabianlee.org/2019/11/18/python-using-flask-to-stream-chunked-dynamic-content-to-end-users/
@app.route(f'/topic/twitter')
def get_messages():
    def events():
        for message in kafka_consumer: 
            yield 'data:{0}\n\n'.format(message.value.decode())
    return Response(events(), mimetype="text/event-stream")

def get_kafka_consumer(): 
    topic = get_kafka_topic()
    consumer = topic.get_simple_consumer(
        auto_offset_reset=OffsetType.LATEST,
        reset_offset_on_start=True
    )
    return consumer

if __name__ == "__main__":
    kafka_consumer = get_kafka_consumer()
    app.run(debug=True, port=5001)
