#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
const char* ssid = "madeyoulook";
const char* password = "eAsierpAss09";
String servername = "https://hackduke2022.aryanmathur4.repl.co/button";
int total = 0;
bool flag = true;
StaticJsonDocument<8192> doc;
        JsonArray jt = doc.createNestedArray("time");
        JsonArray jv = doc.createNestedArray("velocity");
         
void dostuff();
void poststuff(String r);
String printarr(int* x);
int collect(int len);


void setup() {
  pinMode(12, INPUT);
  pinMode(27, INPUT);
  digitalWrite(12, HIGH);
  digitalWrite(27, HIGH);
  Serial.begin(112500);
  WiFi.begin(ssid, password);
    Serial.println("Connecting...");
    while(WiFi.status() != WL_CONNECTED){
        digitalWrite(23, 1);
        delay(250);
        digitalWrite(23,0);
        delay(250);
        Serial.print(".");
      }
     digitalWrite(23, 1);
     Serial.println(WiFi.localIP());
}


void loop() {
      if(digitalRead(27)){
        Serial.println("Test in 3...");
        delay(1000);
        Serial.println("2...");
        delay(1000);
        Serial.println("1...");
        delay(1000);
        Serial.println("BLOW NOW");
        dostuff();
        Serial.println("Done");

        doc["ticks"] = total;
        serializeJson(doc, Serial);
        Serial.println("");
        String request;
        serializeJson(doc, request);
        poststuff(request);
        total=0;
        doc.clear();
        }
        delay(500);
}

void dostuff(){
   int starttime = millis();
   int endtime = starttime;
   while((endtime-starttime)<=7200){
      //Serial.println(endtime);
      float sum = 0;
      for(int k = 0; k < 5; k++){
        //Serial.println(k);
        int c = collect(36);    // get deltas for a period of 5ms
        sum = sum + c;
        total = total+c;
        }
      sum = sum/5;  // Average deltas
      //Serial.print(sum);
      float x = (sum*72*PI/180)/5*0.83;
      //Serial.println(x);
      jv.add(x);    // store avg velocity (in # ticks per 5 milliseconds)
      endtime = millis();
      float y = (endtime-starttime)/1000.0; 
      jt.add(y);
      }
  }

void poststuff(String r){
   HTTPClient http;
    http.begin(servername); 
    http.addHeader("Content-Type","application/json");
    int httpResponseCode = http.POST(r);
      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);
  }

int collect(int len){
  int laststate = digitalRead(12);
  int x = 0;
  int st = millis();
  int et = st;
  while((et-st)< len){
    int newstate = digitalRead(12);
    if(!newstate && laststate){
     x++;
     }
     et = millis();
     laststate = newstate;
    }
    return x;
}
