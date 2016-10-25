from mosquitto import *
from serial import *
from random import *

board = Serial("COM4", 9600, timeout=2)

client = Mosquitto("Rupes96")
client.connect("10.212.61.136")

client.subscribe("/lights")

def messageReceived(broker, obj, msg):
    payload = msg.payload.decode()
    print("Message " + msg.topic + " containing: " + payload)
    
    if (payload == "ON"):
        message = "1"
        board.write(message.encode())
        print("You Just Said On")
    if (payload == "OFF"):
        message = "2"
        board.write(message.encode())
        print("You Just Said Off")

client.on_message = messageReceived

#While the client still exists, ask it to process incoming messages
while (client != None): client.loop()
    