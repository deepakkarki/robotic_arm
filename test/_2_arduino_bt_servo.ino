#include<Servo.h>
int  val; // variable to receive data from the serial port
Servo s;
void setup() 
{
  Serial.begin(9600);       // start serial communication at 9600bps
  s.attach(9);
  s.write(0);
}

void loop() {

  if(Serial.available())
  {
    val = Serial.read();
    s.write(val);
  }
}
