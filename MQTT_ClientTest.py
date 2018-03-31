import paho.mqtt.client as mqtt
import time

#outTopic = "outTopic"
inTopic = "inTopic"
time.sleep(5)

broker_address="192.168.1.117"
print("Create New Instanace")

# http://www.steves-internet-guide.com/into-mqtt-python-client/

client = mqtt.Client("P1") #create new instance
print("connecting to broker")
client.connect(broker_address) #connect to broker
print("Subscribing to topic",inTopic)
client.subscribe(inTopic)
print("Publishing message to topic",inTopic)


while True:
    print ("RED")
    client.publish(inTopic,"Rgb")
    time.sleep(5)
    print ("GREEN")
    client.publish(inTopic,"rGb")
    time.sleep(5)
    print ("BLUE")
    client.publish(inTopic,"rgB")
    time.sleep(5)
