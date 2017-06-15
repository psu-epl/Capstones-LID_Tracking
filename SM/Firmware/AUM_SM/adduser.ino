int adduser(int manid){
//delay here for 10s and wait for another badge in.
int auth = 0;
bool flag = 0;
int wait = 0;

Serial.println("waiting for another badge");


while(!flag && (wait < 10)){





   if((interruptCounter > 5)   && (millis() - lastInterrupt > 25)){
    Serial.println("second badge detected, authenticating");
    int user = wiegand2RFID();
    interruptCounter = 0;
    numberOfInterrupts = 0;  
    auth = sm_add(manid, user);      
    flag = 1;
   }
wait++;

delay(500);
digitalWrite(LEDg, LOW);
delay(500);
digitalWrite(LEDg, HIGH); //active low
  
}  


Serial.print("Got a response to the add request: ");
Serial.println(auth);
  return auth;
  }
