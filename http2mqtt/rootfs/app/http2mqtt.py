import sys, os
from flask import Flask, request, Response
import paho.mqtt.client as mq
from paho.mqtt.client import MQTTErrorCode

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_status():
    return Response("", status=202)

@app.route('/mqtt', methods=['POST'])
def public():
  payload = request.form
  topic = payload.get('topic')
  message = payload.get('payload')
  mqtt.reconnect()
  print(f'Publish to "{topic}" message: "{message}"\n', file=sys.stderr)
  ret = mqtt.publish(topic, message)
  if ret[0] == MQTTErrorCode.MQTT_ERR_SUCCESS:
    return f'OK'
  else:
    print(f"Return: {ret}", file=sys.stderr)
    return Response("{'RET':{ret[0]}}", status=406, mimetype='application/json')

if __name__ == '__main__':
  USERNAME = os.environ.get("MQTT_USERNAME")
  if USERNAME == None:
    print("No username")
    exit(1)
  PASSWORD = os.environ.get("MQTT_PASSWORD")
  SERVER = os.environ.get("MQTT_HOST", "localhost")
  PORT = os.environ.get("MQTT_PORT", 1883)
  mqtt = mq.Client()
  mqtt.username_pw_set(USERNAME, PASSWORD)
  mqtt.connect(SERVER, int(PORT), keepalive=30)
  app.run(debug=False, host="0.0.0.0", port=2883)
