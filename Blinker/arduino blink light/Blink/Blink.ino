// Code inside "setup" gets run once, when the program first starts up
void setup() {
  pinMode(13, OUTPUT);      // Set pin 13 to be in output mode
  Serial.begin(9600);
}

// Code inside "loop" gets run over and over again, once "setup" has finished
void loop() {
  if(Serial.available() > 0) {
    char message = Serial.read();
    if (message == '1'){
      digitalWrite(13, HIGH);
    }
    if (message == '2') {
      digitalWrite(13, LOW);
    }
  }
  

}

 //String on = Serial.readStringUntil('\n');
    //String off = Serial.readStringUntil('\n');
 //Import required libraries
//&  from serial import *

   // Open port by name (different for each device) at a speed of 9600
//& port = Serial("/dev/cu.usbmodem1411",9600,timeout=2) 

   // Clear any previous old data waiting in the buffer
//& port.readall()

   // Write out a string to the serial port
//& message = "Hello there Arduino\n"
//& port.write(message.encode())
//& print("You just said: Hello there Arduino")

    //Read back in and print the response from the serial port, then close it
//& input = port.readline()
//& print("Arduino replied: " + input)
//& port.close()
