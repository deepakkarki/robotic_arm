int  val; 
int led = 13;

void setup()
{
  Serial.begin(9600);
  pinMode(led,OUTPUT);
}

void loop() 
{

  if(Serial.available())
  {
    val = Serial.read();
    if(val=='1')
    {
      digitalWrite(led, HIGH);
    }
    else
    {
      digitalWrite(led, LOW);
    }
  }
  
}
