#include "header.h"


/*
Kle bojo definirani pini kateri bodo povezani na določena vrata,
k ce bojo prtisneni se bo sprozla simulacija kokr ce bi na displayu to prtisnu;
*/

void setup() {
  Serial.begin(9600);
  pinMode(12, OUTPUT);
  pinMode(5, INPUT);
}

void loop() {
  Serial.println("Hello world");
  delay(1000);  
}