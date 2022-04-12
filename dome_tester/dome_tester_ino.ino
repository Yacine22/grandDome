/*********************************************************************
 * Slave arduino : Testing LED blinking in Grand DOME
 * With a Serial communication I2C
 * ____________
 * |            |                    _________
 * |            |    -----SDA-----  | Arduino |
 * |   RASP     |    -----SCL-----  |_ nano___|
 * |            |
 * --------------
 *
*********************************************************************/


#include <Wire.h>

// ----- Parameters -----
int dataReceived, receivedParameters,  dataSent;

#define PIN_DS_DATA 11
#define PIN_STCP_LATCH 10
#define PIN_SHCP_CLOCK 9

#define ledDim 3
#define OE 6
#define clrIo 5

void setup() {

  pinMode(PIN_DS_DATA, OUTPUT);
  pinMode(PIN_STCP_LATCH, OUTPUT);
  pinMode(PIN_SHCP_CLOCK, OUTPUT);

  pinMode(clrIo, OUTPUT);
  pinMode(ledDim, OUTPUT);
  pinMode(OE, OUTPUT);

  Wire.begin(0x44); // Adress of Device !
  Wire.onReceive(receiveLong);
  Wire.onRequest(sendLong);

  analogWrite(ledDim, 75);   // Turn LEDs ON with 75/255 ~ 30%
  digitalWrite(OE, 0);

}

void loop() {
  delay(10);
}

//-------------------------------------------------------------------------

void receiveLong(int) {

  int bytes[sizeof(int)];
  int pbytes[sizeof(int)]; // pbytes refers to parameters


  while (Wire.available()) {

    dataReceived = Wire.read();
    receivedParameters = Wire.read();

    if (dataReceived == 1) {

      digitalWrite(PIN_STCP_LATCH, 0);
      all_off();
      digitalWrite(PIN_STCP_LATCH, 1);

    }

    ////// Using OutPut Enable
    if (dataReceived == 2) {
      
      brightness_with_ledDim(receivedParameters);
      digitalWrite(PIN_STCP_LATCH, 0);
      all_on();
      digitalWrite(PIN_STCP_LATCH, 1);

    }

    ////// Using LedDim
    if (dataReceived == 6) {
      digitalWrite(PIN_STCP_LATCH, 0);
      brightness(receivedParameters);
      all_on();
      digitalWrite(PIN_STCP_LATCH, 1);

    }


    if (dataReceived == 3) {
      //allume_led_x(receivedParameters);

      for (int i = 0; i < sizeof(receivedParameters); i++) {
        allume_led_x(receivedParameters);
        delay(50); /// rajouté ! 
      } 
    }
    
    if (dataReceived == 5) {
      clrIO();
    }
  }

}

void sendLong() {
  dataSent = dataReceived; // return what was recieved --- just to test !!
  byte bytes[sizeof(long)];

  for (int j = 0; j < sizeof(long); ++j)
    bytes[j] = dataSent >> 8 * j;
  Wire.write(bytes, sizeof(long));


}

//--------------------------------------------------------------

void allume_led_x(int x) {
  analogWrite(ledDim, 150);
  int tabled[] = {
    1, 2, 4, 8, 16, 32, 64, 128       };
  digitalWrite(PIN_STCP_LATCH, LOW);
  int bras = x / 8; // shift register
  for (int k = bras + 1; k < 20; k++)
  {
    shiftOut(PIN_DS_DATA, PIN_SHCP_CLOCK, MSBFIRST, B00000000);
  }
  int led = tabled[x % 8];
  shiftOut(PIN_DS_DATA, PIN_SHCP_CLOCK, MSBFIRST, led);

  for (int j = 0; j < bras; j++)
  {
    shiftOut(PIN_DS_DATA, PIN_SHCP_CLOCK, MSBFIRST, B00000000);
  }
  digitalWrite(PIN_STCP_LATCH, HIGH);
}


void all_on() {

  //digitalWrite(ledDim, 1);
  //analogWrite(ledDim, 75);
  digitalWrite(clrIo, 1);
  for (int k = 0; k < 20; k++) {
    shiftOut(PIN_DS_DATA, PIN_SHCP_CLOCK, MSBFIRST, 0xFF);
  }
}

void all_off() {
  analogWrite(ledDim, 0);
  digitalWrite(clrIo, 1);
  for (int k = 0; k < 20; k++) {
    shiftOut(PIN_DS_DATA, PIN_SHCP_CLOCK, MSBFIRST, 0b00000000);
  }

}

void brightness(int brightness) {
  // digitalWrite(ledDim, 0);
  // analogWrite(OE, brightness);
  digitalWrite(OE, 1);
}

void brightness_with_ledDim(int brightness) {
  digitalWrite(OE, 0);
  if (brightness > 150)
  {
    analogWrite(ledDim, 150);
  }
  else{
    analogWrite(ledDim, brightness);
  }

}

void clrIO() {
  digitalWrite(clrIo, 0);
}












