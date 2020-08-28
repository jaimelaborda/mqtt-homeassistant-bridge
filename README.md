# MQTT Homeassitant bridge

This simple piece of code is intended to work as an small bridge between two different MQTT brokers for applications that are not able to connect to two different MQTT brokers at the same time, as for example [HomeAssitant](https://www.home-assistant.io/)

This was the particular need for me but surely it can be addapted and used for many more cases. It also was a very good Python exercise to probe my skills.

It is deprecated even before its creation as I discovered the [Mosquitto MQTT bridge](http://www.steves-internet-guide.com/mosquitto-bridge-configuration/) so I will recommend you to stop reading this and use the Mosquitto MQTT Bridge

Nevertheless the embedded MQTT Bridge is only a valid option if you have access to the MQTT Broker itself (in fact to the mosquitto.conf). So this code will be valid if you have not.

## Configuring it
Edit the sample.config.yml to match your configuration.

* Client source: MQTT broker where you want to source the messages
* Client sink: MQTT broker where you want to source the message

## Running it
It uses Python3 (tested succesfully with 3.8.5).

You will need the following libraries
* [paho-mqtt](https://pypi.org/project/paho-mqtt/)
* [PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation)

Clon this repo and install it with:
```
$ git clone http://github.com/jaimelaborda/mqtt-homeassistant-bridge
$ pip install requirements.txt
```

Then run it with:
```
python ./mqtt-homeassistant-bridge/mqtt-homeassistant-bridge.py
```
