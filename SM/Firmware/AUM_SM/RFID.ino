void setupinterrupt(){
    //Serial.begin(115200); //redundant
  pinMode(data1, INPUT_PULLUP);
  pinMode(data0, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(data1), data1Interrupt, FALLING);
  attachInterrupt(digitalPinToInterrupt(data0), data0Interrupt, FALLING);
  }


  void data1Interrupt() {
  wiegand[interruptCounter] = '1';
  interruptCounter++;
  lastInterrupt = millis();
}



void data0Interrupt() {
  wiegand[interruptCounter] = '0';
  interruptCounter++;
  lastInterrupt = millis();
}




int wiegand2RFID(){
  bool auth = 0;
   int RFID = 0;
  if (interruptCounter ==37){ //for 37 bit HID cards
   
    for (int i=17; i< 36; i++){
      RFID *= 2; // double the result so far
    
  if (wiegand[i] == '1') RFID++;  //add 1 if needed
  }   
}
else;
Serial.print("RFID read!: ");
Serial.println(RFID);

auth = postRFID(RFID);

return auth;
} 
