#define _and  2
#define _nand 3
#define _or  4
#define _nor  10
#define _xor  6
#define _inv  7
#define _sr 11

void setup() {
  Serial.begin(9600);
  for (int i = 2; i<=11;i++){
    pinMode(i, INPUT);
    Serial.println(i);
  }
}
void loop(){
  if (digitalRead(_and)==1){
    Serial.println("and");
  }
  if (digitalRead(_nand)==1){
    Serial.println("nand");
  }
  if (digitalRead(_or)==1){
    Serial.println("or");
  }
  if (digitalRead(_nor)==1){
    Serial.println("nor");
  }
  if (digitalRead(_xor)==1){
    Serial.println("xor");
  }
  if (digitalRead(_inv)==1){
    Serial.println("inv");
  }
  if (digitalRead(_sr)==1){
    Serial.println("sr");
  }
  delay(1000);
}

