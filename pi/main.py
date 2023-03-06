# https://oscarliang.com/connect-raspberry-pi-and-arduino-usb-cable/
import serial
import util


ser = serial.Serial('/dev/ttyUSB0', 9600)

#util.Messages.Terminal.init
ser.write('Hello from Raspberry Pi!'.encode())

# 1. ui k bo skos przgan da se ne vid pac oz da se ne more exitat (plus ma gumbke za izbiro vrat in pol odpre novo okno za opravljanje vrat),
# 2. nek fail-safe k se sproz ce se zapre ta program (aka se ne backproces k checka ce ta program deluje al ne (aka bash shit )) -> sproz da se al restarta program al pa sam ugasne,
# 3. funkcija k bo tejkala care za predvajanje videa (ce se prtisne gumb pr XOR vratih da pol predvaja npr: XOR.mp4 na loopu za tko idk x sekund; pol pa se vrne nazaj na prvortn ui),
# 4. funkcija k bo komunicirala z arduinotom (če se tm zazna da se ksn gumb prtisne da se to poročin in posledično predvaja simulacija)
def do_smthing(v):
    if type(v) == int:
        if v == 1:
            print("vrata so bla bla")
            import time
            time.sleep(5)
    else:pass
while True:
    if ser.in_waiting > 0:
        message = ser.readline().strip().decode('utf-8')  # read the message from serial
        #print(message)  # print the message to the console
        import time
        ct =time.strftime("%H:%M")
        log_rep = f"[at {ct}]\nSerial data: {ser}\nDecoded message: {message}"
        with open("log.log", "a") as file:
            file.write(log_rep)
        do_smthing(message)
