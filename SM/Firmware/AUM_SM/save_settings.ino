#include <EEPROM.h>

void clear_eeprom(){
  Serial.println("Clearing EEPROM");
  for (int i = 0 ; i < 512 ; i++) {
    EEPROM.write(i, 0);
  }
  delay(100);
  EEPROM.commit();
  delay(100);
}


void read_settings(){ //read settings and copy to global strings
 Serial.println("Reading EEPROM");
  Serial.println("Reading EEPROM host:");
  String host_r =""; //use global?
  for (int i = 0; i < 40; ++i)
    {
      host_r += char(EEPROM.read(i));
    }  
    
    delay(100); //for reliability
    
  Serial.print("Host: ");
  Serial.println(host_r);

  Serial.println("Reading EEPROM SMID");
  String SMID_r = "";
  for (int i = 40; i < 80; ++i)
    {
      SMID_r += char(EEPROM.read(i));
    }

    delay(100); //for reliability
    
  Serial.print("SMID: ");
  Serial.println(SMID_r);  

  Serial.println("Reading EEPROM path");
 String path_r = "";
  for (int i = 80; i < 120; ++i)
    {
      path += char(EEPROM.read(i));
    }
  Serial.print("Path: ");
  Serial.println(path_r);  
  
  delay(100); // I guess you have to have a delay here for it to work..didn't work without it
 
 Serial.println("Reading EEPROM done");

//copy to global, didn't work other way, should be fixed
path = path_r;
SMID = SMID_r;
host = host_r;
 
  }



void write_settings(){     //copy strings back to struct and write to EEPROM
  Serial.println("writing settings to EEPROM");
  clear_eeprom();
  delay(100);
          Serial.println("writing eeprom host:");
          for (int i = 0; i < host.length(); ++i)
            {
              EEPROM.put(i, host[i]);
              Serial.print("Wrote: ");
              Serial.println(host[i]); 
            }
            delay(100);
            EEPROM.commit();
            delay(100);
            
          Serial.println("writing eeprom SMID:"); 
          for (int i = 0; i < SMID.length(); ++i)
            {
              EEPROM.put(40+i, SMID[i]);
              Serial.print("Wrote: ");
              Serial.println(SMID[i]); 
            }    
delay(100);
EEPROM.commit();
            delay(100);

          Serial.println("writing eeprom path"); 
          for (int i = 0; i < path.length(); ++i)
            {
              EEPROM.put(80+i, path[i]);
              Serial.print("Wrote: ");
              Serial.println(path[i]); 
            }    
         
         delay(100); 
         EEPROM.commit();
        delay(100);



  }


void compare_settings(){
  Serial.println("Comparing settings");

 
  Serial.print("SMID: ");
  Serial.println(SMID);
  Serial.println(SMIDc);
  Serial.print("Host: ");
  Serial.println(host);
  Serial.println(hostc);
  Serial.print("Path: ");
  Serial.println(path);
  Serial.println(pathc);


if ((SMID == String(SMIDc)) && (host==String(hostc)) && (path==String(pathc))){
  Serial.println("Good to go, settings not changed");
  }else{
    Serial.println("Settings changed, writing settings");
    //setupchar2string();
    write_settings(); 
    }



  
  }    

void setupstring2char(){
SMID.toCharArray(SMIDc, SMID.length()+1);
host.toCharArray(hostc, host.length()+1);
path.toCharArray(pathc, path.length()+1);

Serial.println("Copied strings to char arrays, STRINGS:");
Serial.println(SMID);
Serial.println(host);
Serial.println(path);

Serial.println("Chars:");
Serial.println(SMIDc);
Serial.println(hostc);
Serial.println(pathc);
Serial.println("--> DONE <--");
  
  
  }



void setupchar2string(){
  SMID = String(SMIDc);
  host = String(hostc);
 path = String(path);

Serial.println("Copied chars to strings");

Serial.println(SMID);
Serial.println(host);
Serial.println(path);
Serial.println("--> DONE <--");
  
  
  
  }  
