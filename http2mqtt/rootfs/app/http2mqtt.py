import sys, os
from flask import Flask, request, Response
import paho.mqtt.client as mq
from paho.mqtt.client import MQTTErrorCode
from random import random as rnd

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_status():
    return Response("", status=202)

@app.route('/mqtt', methods=['POST'])
def public():
  payload = request.form
  topic = payload.get('topic')
  message = payload.get('payload')
  print(f'Publish to "{topic}" message: "{message}"', file=sys.stderr, end=" ... ")
  ret = mqtt.publish(topic, message)
  if ret[0] == MQTTErrorCode.MQTT_ERR_SUCCESS:
    print("OK", file=sys.stderr)
    return f'OK'
  else:
    print(f"Error: {ret}", file=sys.stderr)
    return Response("{'RET':{ret[0]}}", status=406, mimetype='application/json')

def on_connect(client, userdata, flags, reason_code, properties):
  if "Success" == reason_code:
    print(f"Client ({client_id}) successfully connected to MQTT broker", file=sys.stderr)
  else:
    print(f"Error connect to MQTT broker. Reason: {reason_code}", file=sys.stderr)
    quit(1)

USERNAME = os.environ.get("MQTT_USERNAME")
if USERNAME == None:
  print("No username", file=sys.stderr)
  exit(1)
PASSWORD = os.environ.get("MQTT_PASSWORD")
SERVER = os.environ.get("MQTT_HOST", "localhost")
PORT = os.environ.get("MQTT_PORT", 1883)
client_id = f"http2mqtt-{int(rnd()*0xFFFFFF):06x}"
mqtt = mq.Client(mq.CallbackAPIVersion.VERSION2, client_id)
mqtt.on_connect = on_connect
mqtt.username_pw_set(USERNAME, PASSWORD)
mqtt.connect(SERVER, int(PORT), keepalive=30)
# print("MQTT Client ID:", client_id)
mqtt.loop_start()

if __name__ == '__main__':
  app.run(debug=False, host="0.0.0.0", port=2883)
  mqtt.loop_stop()
