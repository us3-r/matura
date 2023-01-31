#include <string>

void ConformityCheck(int pass) {
    int count_pass = 0;
    int count_fail = 0;
    while (count_pass < pass) {
        if (Serial.available()) {
            String value = Serial.readString().decode();
            Serial.println(value);
            count_pass++;
        }
        else{
            TerminalPrint("[!] No data received ");
            count_fail++;
        }
    }
    if (count_fail > int(pass/2)) {
        TerminalPrint("[!] Connection failed");
        reset();
    }
    else {
        TerminalPrint("[+] Connection established");
    }
}

void TerminalPrint(String text){
    Serial.println("[$] ",text);
}

void (* reset) (void) = 0; // reset function at address 0