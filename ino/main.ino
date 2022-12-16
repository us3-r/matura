#include "header.h"

void setup() {
	Serial.begin(9600);
	TerminalPrint(" Arduino is started ...");
}

void loop() {
	// put your main code here, to run repeatedly:
	ConformityCheck();
}