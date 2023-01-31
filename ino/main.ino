#include "header.h"


/*
Kle bojo definirani pini kateri bodo povezani na določena vrata,
k ce bojo prtisneni se bo sprozla simulacija kokr ce bi na displayu to prtisnu;
*/

void setup() {
	Serial.begin(9600);
	TerminalPrint(" Arduino is started ...");
	ConformityCheck(5);  					// prever ce sta arduono in rasberry povezana
}

void loop() {
	/*
	1. funkcija za komuniciranje z razberijem (prebere vrednost ker pin je treba dt na high da bojo tista vrata delala)
	2. uporaba switch case zato da bo speed pa pac ker lah
	*/
}