#include <ESP8266WiFi.h>          //ESP8266 Core WiFi Library
#include <EEPROM.h>
#include <DNSServer.h>            //Local DNS Server used for redirecting all requests to the configuration portal
#include <ESP8266WebServer.h>     //Local WebServer used to serve the configuration portal
#include <WiFiManager.h>          //https://github.com/tzapu/WiFiManager WiFi Configuration Magic
#include <string.h>

//IO stuff
const byte data0 = 5;  //RFID DATA0 on this pin (wiegand protocol)
const byte data1 = 4;  //RFID DATA1 on this one
const byte APD = 15; // power switch pin
const byte LEDg = 0; //green LED
const byte BEEP = 2;  //Audible alarm
//const byte SS1 = 1;  //unused
//const byte SS2 = 3;
//const byte MOSI = 12;
//const byte MISO = 13;
//const byte SPICLK = 14;

int ADCthreshold = 300;   //ADC used as digitial IO, set threshold here 0-1024

//interrupt things
byte interruptCounter = 0;
int numberOfInterrupts = 0;
char wiegand[50];
unsigned long lastInterrupt =0;
//int wiegand2RFID(); 






 String SMID = "2dd2bde1-750c-46fe-af68-5796a2bfbd0e"; // hardcoded for now
//const char* host = "aummanage.com";  //hardcoded for now
 String host = "aummanage.com";  //hardcoded for now//try this
 String path = "/aum";  //hardcoded for now

 
 char SMIDc[40];
 char hostc[40];
 char pathc[40];





void setup() {
  Serial.begin(115200);
  
    
 //EEPROM.begin(512);
//  delay(10);
//read_settings();
setupstring2char();

  String s = WiFi.macAddress();
  Serial.println("");
  Serial.println("MAC ADDRESS: ");
  Serial.println(s);

  
  delay(1000);
  setupWIFI();
 


  //setup IO
  pinMode(APD, OUTPUT);
  digitalWrite(APD, LOW); //active high
  pinMode(BEEP, OUTPUT);
  digitalWrite(BEEP, HIGH);  //active low
  pinMode(LEDg, OUTPUT);
  digitalWrite(LEDg, HIGH); //active low

Serial.println("compare settings:");

//compare_settings();

 setupinterrupt();
}





void loop(){
  
  static bool auth = 0;
  static int RFID = 0;
  static int manid = 0;
  
      if((interruptCounter > 5)   && (millis() - lastInterrupt > 25)){

        if (analogRead(A0) > ADCthreshold) {  
          Serial.println("Add user requested!");       
          manid = wiegand2RFID();
          adduser(manid);
          
          }
        else { RFID = wiegand2RFID();
         auth = postRFID(RFID);

        }
        
        
        
        Serial.print("AUTH = ");
        Serial.println(auth);
        interruptCounter = 0;
        if (auth == 1){
          Serial.println("APD enabled");
        }
        else beepslow(1);
        }


      if   ((analogRead(A0) > ADCthreshold) && (auth == 1)){
        auth = 0;
        digitalWrite(APD,LOW); //don't wait for confermation to turn off 
        beepfast(1);
        Serial.println("Logout");
        beepfast(2);
        logout();

        digitalWrite(LEDg, HIGH); //turn off green light
        digitalWrite(BEEP, HIGH); 
        
      } 
      else;


      if (auth == 1){      
        digitalWrite(APD,HIGH);
        digitalWrite(LEDg, LOW);//active low  
      }
      
      else { 
        digitalWrite(APD,LOW);
        digitalWrite(LEDg, HIGH);
       }
}

void beepfast(int beepy){
        for (int i = 0; i < beepy; i++){
        digitalWrite(BEEP, LOW); //turn on
        delay(100);
        digitalWrite(BEEP, HIGH); //turn off now
        delay(100);
        }
        
}

void beepslow(int beepy){
        for (int i = 0; i < beepy; i++){
        digitalWrite(BEEP, LOW); //turn off now
        delay(500);
        digitalWrite(BEEP, HIGH); //turn off now
        delay(500);
        }
 
}

