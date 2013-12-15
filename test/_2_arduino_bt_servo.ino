#include<Servo.h>
int  val; 
// variable to receive data from the serial port
Servo s;
//A servo object

void setup() 
{
  Serial.begin(9600);       
  // start serial communication at 9600bps
  s.attach(9);
  //attach the servo object at port 9
  s.write(0);
}

void loop() {
//infinite loop 

  if(Serial.available())
  //check is serial data is available
  {
    val = Serial.read();
    //read the value 
    s.write(val);
    //write the value to the servo
  }
}
