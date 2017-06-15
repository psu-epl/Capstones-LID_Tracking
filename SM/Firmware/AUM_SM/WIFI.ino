void setupWIFI(){
  
//Add custom parameter SMID to setup  
WiFiManagerParameter custom_smid("SMID", "Station ID", SMIDc , 40);
WiFiManagerParameter custom_host("Host", "Host Name", hostc , 40);
WiFiManagerParameter custom_path("Path", "path", pathc , 40);


WiFiManager wifiManager;
//wifiManager.setSaveConfigCallback(saveConfigCallback);  //not needed
wifiManager.addParameter(&custom_smid);
wifiManager.addParameter(&custom_host);
wifiManager.addParameter(&custom_path);



//Allow setup any time by pressing STOP during power up
  if   (analogRead(A0) > ADCthreshold){
    wifiManager.resetSettings(); //for testing
    wifiManager.startConfigPortal("AUM_Station_Module");}
else {wifiManager.autoConnect("AUM_Station_Module");}




  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }



//copy wifi setup values to global values (they were loaded with WiFiManagerParameter)
  Serial.println("");
  Serial.println("WiFi connected");  
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.print("SMID: ");
  Serial.println(custom_smid.getValue());
  Serial.print("Host: ");
  Serial.println(custom_host.getValue());
  Serial.print("Path: ");
  Serial.println(custom_path.getValue());


  SMID = String(custom_smid.getValue());
  host = String(custom_host.getValue());
  path = String(custom_path.getValue());

  

  
  }
