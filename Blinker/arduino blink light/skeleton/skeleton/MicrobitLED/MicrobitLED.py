from microbit import *

uart.write("Ready\n")
while(True):
    if(uart.any()):
        input = uart.read(1)
        next_character = chr(input[0])
        print("You just sent: " + next_character)
