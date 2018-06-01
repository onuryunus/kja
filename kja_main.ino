#include <SPI.h>
#include <SD.h>
#include <ADXL345dual.h>
#include <Wire.h>


File myFile;
ADXL345 device;
String fileName = String();
int firstsensor = 0;
int secondsensor = 1;
int Cs = 8;
int Button_start = 2 ;
int Button_stop = 3 ;
int start_led = 5;
int Sdo = 9;
volatile bool recycle;
int Buzzer = 6;

void setup() {
  recycle = false ;

  Serial.begin(9600);

  Serial.println("SD kart yukleniyor.");
  if (!SD.begin(10)) {
    Serial.println("Yukleme basarisiz!");
    while (1);
  }
  Serial.println("SD kart yukleme basarılı.");
  
  pinMode(Buzzer, OUTPUT);
  pinMode(Cs, OUTPUT);
  digitalWrite(Cs, HIGH);
  pinMode(Sdo, OUTPUT);
  digitalWrite(Sdo, HIGH);
  pinMode(Button_start, INPUT_PULLUP);
  pinMode(Button_stop, INPUT_PULLUP);

  device.begin(firstsensor);
  device.setDataRate(firstsensor, ADXL345_DATARATE_200HZ);
  device.setRange(firstsensor, ADXL345_RANGE_2G);

  device.begin(secondsensor);
  device.setDataRate(secondsensor, ADXL345_DATARATE_200HZ);
  device.setRange(secondsensor, ADXL345_RANGE_2G);
  
  if (!device.begin(firstsensor))
  {
    Serial.println("Sensor yüklenemedi.");
    delay(500);
  }
  if (!device.begin(secondsensor))
  {
    Serial.println("bulunamadı");
    delay(500);
  }
}

void loop() {
  if (!digitalRead(Button_start))
  {
    recycle = true;
    delay(10);
    initSD();
    startled();
    delay(10);
    myFile = SD.open(fileName, FILE_WRITE);
    bip();
  }
  if (!digitalRead(Button_stop))
  {
    recycle = false;
    delay(10);
    myFile.close();
    bip();
  }
  if ( recycle )
  {
    if (myFile)
    {
      char data[32];
      Vector raw1 = device.readRaw(firstsensor);
      Vector raw2 = device.readRaw(secondsensor);
      sprintf(data, "%d,%d,%d,%d,%d,%d", int(raw1.XAxis), int(raw1.YAxis), int(raw1.ZAxis), int(raw2.XAxis), int(raw2.YAxis), int(raw2.ZAxis));
      Serial.println(data);
      myFile.println(data);
      delay(10);
    }
    else {
      Serial.println("error opening test.txt");
    }
  }
  delay(10);
}

void bip()
{
  digitalWrite(Buzzer, HIGH);
  delay(100);
  digitalWrite(Buzzer, LOW);
}

void initSD() {

  unsigned int filenumber = 1;
  while (!filenumber == 0) {
    fileName = "Da_";
    fileName += filenumber;
    fileName += ".txt";

    while (SD.exists(fileName)) {
      filenumber++;
      fileName = "Da_";
      fileName += filenumber;
      fileName += ".txt";
    }
    myFile = SD.open(fileName, FILE_WRITE);
    myFile.close();
    return;
  }
}

void startled()
{
  digitalWrite(start_led, HIGH);
  delay(10);
  digitalWrite(start_led, LOW);
  delay(90);
}
