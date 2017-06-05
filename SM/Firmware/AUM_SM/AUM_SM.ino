#include <ESP8266WiFi.h>          //ESP8266 Core WiFi Library (you most likely already have this in your sketch)
#include <EEPROM.h>
#include <DNSServer.h>            //Local DNS Server used for redirecting all requests to the configuration portal
#include <ESP8266WebServer.h>     //Local WebServer used to serve the configuration portal
#include <WiFiManager.h>          //https://github.com/tzapu/WiFiManager WiFi Configuration Magic

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
int wiegand2RFID(); //do you need to declare func in ardu ide?





String SMID = "2dd2bde1-750c-46fe-af68-5796a2bfbd0e"; // hardcoded for now
char SMIDc[] = "2dd2bde1-750c-46fe-af68-5796a2bfbd0e"; //why do I need two... find and reduce to one 
const char* host = "aummanage.com";  //hardcoded for now
String path = "/aum/auth";  //hardcoded for now





void setup() {
  
  Serial.begin(115200);
  delay(1000);
  setupWIFI();
  setupinterrupt();
  
  pinMode(APD, OUTPUT);
  digitalWrite(APD, LOW); //active high
  pinMode(BEEP, OUTPUT);
  digitalWrite(BEEP, HIGH);  //active low
  pinMode(LEDg, OUTPUT);
  digitalWrite(LEDg, HIGH); //active low

}





void loop(){
  
  static bool auth = 0;
  
      if((interruptCounter > 5)   && (millis() - lastInterrupt > 25)){
        auth = (wiegand2RFID());
        Serial.print("AUTH = ");
        Serial.println(auth);
        interruptCounter = 0;
        if (auth == 1){
          Serial.println("APD enabled");
        }
        else beepthismany(5);
        }


      

      if   ((analogRead(A0) > ADCthreshold) && (auth == 1)){
        auth = 0;
        Serial.println("Logout");
        //call logout function?  
        digitalWrite(BEEP, LOW); //active low
        delay(100); //logout sound
        digitalWrite(LEDg, HIGH); //active low
        digitalWrite(BEEP, HIGH); //turn off now
        
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


void beepthismany(int beepy){
        for (int i = 0; i < beepy; i++){
        digitalWrite(BEEP, LOW); //turn off now
        delay(500);
        digitalWrite(BEEP, HIGH); //turn off now
        delay(500);
  
        }
  
  return;
 
}

