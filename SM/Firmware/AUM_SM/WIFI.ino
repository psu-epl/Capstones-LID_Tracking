void setupWIFI(){
  
  
  
  
/* // Will set this up later.. hard coded SMID for now.
//read SMID information out of EEPROM
EEPROM.begin(512);
Serial.println("Reading EEPROM SMID");
  String esmid = "";
  for (int i = 0; i < 40; ++i)
    {
      epass += char(EEPROM.read(i));
    }

  Serial.print("esid: ");
  Serial.println(esmid);
*/








//Add custom parameter SMID to setup  
WiFiManagerParameter custom_smid("SMID", "Station ID", SMIDc , 40);
WiFiManager wifiManager;
//wifiManager.setSaveConfigCallback(saveConfigCallback);  //not needed
wifiManager.addParameter(&custom_smid);

//Allow setup any time by pressing STOP during power up
  if   (analogRead(A0) > ADCthreshold){
    //wifiManager.resetSettings(); //for testing
    wifiManager.startConfigPortal("AUM_Station_Module");}
else {wifiManager.autoConnect("AUM_Station_Module");}

/*  //EEprom stuff
 *   
if (custom_smid.getValue() != esid){ 
  
  Serial.println("doing some stuffffffff......");


String temp = custom_smid.getValue();
Serial.print("temp: ");
Serial.println(temp);

temp.toCharArray(esid, 40);

Serial.print("temp length ");
Serial.println(sizeof(temp));
Serial.print("esid length ");
Serial.println(sizeof(esid));


        for (int i = 0; i < 40; ++i)  //Dont write to EEPROM yet.  wiill do later
          {
            EEPROM.write(i, esid[i]);
            Serial.print("Wrote: ");
            Serial.println(esid[i]); 
          }

           }
*/



  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");  
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.print("SMID: ");
  Serial.println(custom_smid.getValue());
  

  
  }
