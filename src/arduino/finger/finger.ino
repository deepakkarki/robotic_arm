#include<Servo.h>
int  val; 
// variable to receive data from the serial port
Servo s1;
Servo s2;
Servo s3;
Servo s4;
Servo s5;
//A servo object

void setup() 
{
  Serial.begin(9600);       
  // start serial communication at 9600bps
  s1.attach(11); //thumb
  s2.attach(9); //pointing
  s3.attach(6); //middle
  s4.attach(10); //ring
  s5.attach(5); //little
  //attach the servo object at port 9
  s1.write(0);
  s2.write(0);
  s3.write(0);
  s4.write(0);
  s5.write(0);
}

void loop() {
//infinite loop 

  if(Serial.available())
  //check is serial data is available
  {
    val = Serial.read();
    s1.write(val);
    s2.write(val);
    s3.write(val);
    s4.write(val);
    s5.write(val);
  }
}
