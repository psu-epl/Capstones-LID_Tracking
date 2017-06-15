#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>

// Use WiFiClient class to create TCP connections
WiFiClient client;

bool postRFID(int RFID) {
String str = "";
String RFIDs = String(RFID); //convert RFID to string to pass to client
String hosts = String(host);
bool auth = 0;

  Serial.print("connecting to ");
  Serial.println(host);

  if (client.connect(hostc, 80)) {
    Serial.println("Connection Established with" + hosts);
  }else {
    Serial.println("connection failed");
    return 0;
  }


String PostData = "SMID=" + SMID + "&RFID=" + RFIDs;

//String PostData = "SMID=2dd2bde1-750c-46fe-af68-5796a2bfbd0e&RFID=174470";

client.println("POST " + path + "/sm_login" + " HTTP/1.1");
client.println("Host: "+ hosts);
client.println("Cache-Control: no-cache");
client.println("Content-Type: application/x-www-form-urlencoded");
client.print("Content-Length: ");
client.println(PostData.length());
client.println();
client.println(PostData);
long interval = 2000;
unsigned long currentMillis = millis(), previousMillis = millis();

while(!client.available()){

  if( (currentMillis - previousMillis) > interval ){

    Serial.println("Timeout");
    client.stop();     
    return 0;
  }
  currentMillis = millis();
}

int id1 = 0;
while (client.connected()){
  
  if ( client.available() ){
    str=client.readStringUntil('\n');
    Serial.print(id1);
    Serial.print(" ");
    id1++;
    Serial.print(str);}
      
      
      if (str == "False"){
        Serial.println("Gota false");
       break;}
       else if (str == "True"){
        Serial.println("Gota true!");
        break;}
        else;
        
}   

   
  if (client.connected()) { 
    client.stop();  // DISCONNECT FROM THE SERVER
  }
  Serial.println();
  Serial.println("closing connectionnnnn");
  client.stop();

Serial.print("SERVER RETURNED: ");
Serial.println(str);
if (str == "True"){
  auth = 1;}
else {
  auth = 0;}




  
return (auth);
}



bool sm_add(int manid,int user) {
String str = "";
String mgr = String(manid);
String RFIDs = String(user);//convert RFID to string to pass to client
String hosts = String(host);
bool auth = 0;

  Serial.print("connecting to ");
  Serial.println(host);

  if (client.connect(hostc, 80)) {
    Serial.println("Connection Established with" + hosts);
  }else {
    Serial.println("connection failed");
    return 0;
  }


String PostData = "smid=" + SMID + "&mgr=" + mgr + "&user=" + RFIDs;
Serial.print("Post data is: ");
Serial.println(PostData);
//String PostData = "SMID=2dd2bde1-750c-46fe-af68-5796a2bfbd0e&RFID=174470";

client.println("POST " + path + "/sm_add/" + " HTTP/1.1");
client.println("Host: "+ hosts);
client.println("Cache-Control: no-cache");
client.println("Content-Type: application/x-www-form-urlencoded");
client.print("Content-Length: ");
client.println(PostData.length());
client.println();
client.println(PostData);
long interval = 2000;
unsigned long currentMillis = millis(), previousMillis = millis();

while(!client.available()){

  if( (currentMillis - previousMillis) > interval ){

    Serial.println("Timeout");
    client.stop();     
    return 0;
  }
  currentMillis = millis();
}

int id1 = 0;
while (client.connected()){
  
  if ( client.available() ){
    str=client.readStringUntil('\n');
    Serial.print(id1);
    Serial.print(" ");
    id1++;
    Serial.print(str);}
      
      
      if (str == "False"){
        Serial.println("Gota false");
       break;}
       else if (str == "True"){
        Serial.println("Gota true!");
        break;}
        else;
        
}   

   
  if (client.connected()) { 
    client.stop();  // DISCONNECT FROM THE SERVER
  }
  Serial.println();
  Serial.println("closing connectionnnnn");
  client.stop();

Serial.print("SERVER RETURNED: ");
Serial.println(str);
if (str == "True"){
  auth = 1;}
else {
  auth = 0;}

  
return (auth);
}












void logout(){
String hosts = String(host);
  Serial.print("connecting to ");
  Serial.println(host);

  if (client.connect(hostc, 80)) {
    Serial.println("Connection Established with" + hosts);
  }else {
    Serial.println("connection failed");
  }


String PostData = "SMID=" + SMID;

//String PostData = "SMID=2dd2bde1-750c-46fe-af68-5796a2bfbd0e&RFID=174470";

client.println("POST " + path +"/sm_logout" +" HTTP/1.1");
client.println("Host: "+ hosts);
client.println("Cache-Control: no-cache");
client.println("Content-Type: application/x-www-form-urlencoded");
client.print("Content-Length: ");
client.println(PostData.length());
client.println();
client.println(PostData);
long interval = 2000;
unsigned long currentMillis = millis(), previousMillis = millis();

while(!client.available()){

  if( (currentMillis - previousMillis) > interval ){

    Serial.println("Timeout");
    client.stop();     
  }
  currentMillis = millis();
}

  
 if (client.connected()) { 
    client.stop();  // DISCONNECT FROM THE SERVER
  }
  Serial.println();
  Serial.println("closing connectionnnnn");
  client.stop();

Serial.println("Logged out");
}



