import yaml
import paho.mqtt.client as mqtt

def read_config(file):
    with open(file) as f:
        docs = yaml.load(f)

        global mqtt_source
        global mqtt_sink

        mqtt_source = docs["mqtt-source"]
        mqtt_sink = docs["mqtt-sink"]

def client_source_on_connect(client, userdata, flags, rc):
    print(f"Client_Source: Client {client} succesfully connected with result code {rc}")

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(mqtt_source["topic"]) # Subscribe to all

def client_sink_on_connect(client, userdata, flags, rc):
    print(f"Client_Sink: Client {client} succesfully connected with result code {rc}")

    #client.subscribe("$SYS/#")

def client_source_on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    client_sink.publish(msg.topic, payload=msg.payload, qos=0, retain=False)

if __name__ == "__main__":
    read_config('config.yml') # Read config from config.yml

    client_source = mqtt.Client()
    client_sink = mqtt.Client()

    client_source.on_connect = client_source_on_connect
    client_sink.on_connect = client_sink_on_connect

    # Connect mqtt clients
    client_source.username_pw_set(mqtt_source["user"], mqtt_source["password"])
    client_source.connect(mqtt_source["host"], mqtt_source["port"], 60)

    client_sink.username_pw_set(mqtt_sink["user"], mqtt_sink["password"])
    client_sink.connect(mqtt_sink["host"], mqtt_sink["port"], 60)

    client_source.on_message = client_source_on_message


    while(1):
        # Run the client loops
        client_source.loop()
        client_sink.loop()

    

