#include <EEPROM.h>
#include <SoftwareSerial.h>
#include <SPI.h>
#include <SD.h>
#include <ADXL345dual.h>
#include <Wire.h>

File myFile;
ADXL345 device;
String fileName = String();
const int rxpin = 7;
const int txpin = 6;
char k = 'A';
unsigned int filenumber;
SoftwareSerial bluetooth(rxpin, txpin);
int Sdo = 9;
int Cs = 8;
int Button_start = 2 ;
int Button_stop = 4 ;
int Button_bluetooth = 3;
int buzzer = 5;
int firstsensor = 0;
int secondsensor = 1;
volatile bool recycle;
char inputString [100];
char inputChar;
int stringIndex = 0;
void setup()
{
  recycle = false;
  pinMode(Cs, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(buzzer, OUTPUT);
  digitalWrite(Cs, HIGH);
  pinMode(Sdo, OUTPUT);
  digitalWrite(Sdo, HIGH);
  pinMode(Button_start, INPUT_PULLUP);
  pinMode(Button_stop, INPUT_PULLUP);
  pinMode(Button_bluetooth, INPUT_PULLUP);

  Serial.begin(9600);
  Serial.println("SD kart yukleniyor.");
  if (!SD.begin(10)) {
    Serial.println("Yukleme basarisiz!");
    while (1);
  }
  Serial.println("SD kart yukleme basarılı.");
  bluetooth.begin(115200);

  device.begin(firstsensor);
  device.setDataRate(firstsensor, ADXL345_DATARATE_200HZ);
  device.setRange(firstsensor, ADXL345_RANGE_2G);

  device.begin(secondsensor);
  device.setDataRate(secondsensor, ADXL345_DATARATE_200HZ);
  device.setRange(secondsensor, ADXL345_RANGE_2G);
}

void loop() {

  if (!digitalRead(Button_start))
  {
    recycle = true;
    delay(10);
    initSD();
    delay(10);
    myFile = SD.open(fileName, FILE_WRITE);
    beep();
  }
  if (!digitalRead(Button_stop))
  {
    recycle = false;
    delay(10);
    myFile.close();
    beep();

  }

  if (!digitalRead(Button_bluetooth))
  {
    recycle = false;
    beep();
    unsigned long start;
    start = millis();
    while (( millis() - start) < 30000)
    {
      if (bluetooth.available())
      {
        k = bluetooth.read();
        if ( k == 'H' )
        {

          EEPROM.get(0, filenumber);
          fileName = "Ex_";
          fileName += filenumber;
          fileName += ".txt";
          Serial.println("Sending...");
          myFile = SD.open(fileName);
          if (myFile)
          {
            while (myFile.available())
            {

              bluetooth.write(myFile.read() );
              delay(1);

            }
            myFile.close();
          }
          Serial.print('T');
        }
      }
      else
        Serial.println("No DATA");
      delay(1);
    }
    Serial.print("TIME OUT");
  }
  if (recycle)
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
}

void initSD()
{
  unsigned int filenumber = 1;
  while (!filenumber == 0) {
    fileName = "Ex_";
    fileName += filenumber;
    fileName += ".txt";

    while (SD.exists(fileName)) {
      filenumber++;
      fileName = "Ex_";
      fileName += filenumber;
      fileName += ".txt";
    }
    EEPROM.put(0, filenumber);
    myFile = SD.open(fileName, FILE_WRITE);
    myFile.close();
    return;
  }
}

void beep()
{
  digitalWrite(buzzer, HIGH);
  delay(100);
  digitalWrite(buzzer, LOW);
}
