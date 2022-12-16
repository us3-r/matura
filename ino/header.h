#include <string>

void ConformityCheck(int pass=4) {
    int count_pass = 0;
    while (count_pass < pass) {
        if (Serial.available()) {
            String value = Serial.readString().decode();
            Serial.println(value);
            count_pass++;
        }
        else{
            TerminalPrint("[!] No data received");
        }
    }
}

void TerminalPrint(String text){
    Serial.println("[$] ",text);
}