# https://oscarliang.com/connect-raspberry-pi-and-arduino-usb-cable/
import serial
from util import Start


ser = serial.Serial('/dev/ttyUSB0', 9600)

#util.Messages.Terminal.init
ser.write('Hello from Raspberry Pi!'.encode())

# 1. ui k bo skos przgan da se ne vid pac oz da se ne more exitat (plus ma gumbke za izbiro vrat in pol odpre novo okno za opravljanje vrat),
# 2. nek fail-safe k se sproz ce se zapre ta program (aka se ne backproces k checka ce ta program deluje al ne (aka bash shit )) -> sproz da se al restarta program al pa sam ugasne,
# 3. funkcija k bo tejkala care za predvajanje videa (ce se prtisne gumb pr XOR vratih da pol predvaja npr: XOR.mp4 na loopu za tko idk x sekund; pol pa se vrne nazaj na prvortn ui),
# 4. funkcija k bo komunicirala z arduinotom (če se tm zazna da se ksn gumb prtisne da se to poročin in posledično predvaja simulacija)
def get_video(select :str):
    import os
    gate_list = [
        "and",
        "nand",
        "or",
        "nor",
        "xor",
        "inv",
        "sr"
    ]
    path = f"anim/{select}.mp4" if select in gate_list else None
    print(path)
    #if path is not None: os.system(f"vlc --play-and-exit {path}")

Start.init_check()

while True:
    if ser.in_waiting > 0:
        message = ser.readline().strip().decode('utf-8')  # read the message from serial
        #print(message)  # print the message to the console
        import time
        ct =time.strftime("%H:%M")
        log_rep = f"[ at {ct} ]\nSerial data: {ser}\nDecoded message: {message}\n"
        with open("log.log", "a") as file:
            file.write(log_rep)
        get_video(message)
