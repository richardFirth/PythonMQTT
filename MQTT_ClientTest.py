import paho.mqtt.client as mqtt

# http://www.steves-internet-guide.com/into-mqtt-python-client/


Client(client_id="Client1",clean_session=True, userdata=None, protocol=MQTTv311, transport=”tcp”)

client =mqtt.Client(client_name)

connect(host, port=1883, keepalive=60, bind_address="")
