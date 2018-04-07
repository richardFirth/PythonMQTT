import paho.mqtt.client as mqtt

# https://pypi.python.org/pypi/paho-mqtt/1.3.1
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("outTopic")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


#outTopic = "outTopic"
inTopic = "inTopic"


broker_address="192.168.1.117"
print("Create New Instanace")

# http://www.steves-internet-guide.com/into-mqtt-python-client/

client = mqtt.Client("P1") #create new instance
client.on_connect = on_connect
client.on_message = on_message
print("connecting to broker")
client.connect(broker_address) #connect to broker
print("Subscribing to topic",inTopic)
#client.subscribe(inTopic)
#print("Publishing message to topic",inTopic)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
