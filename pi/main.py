# https://oscarliang.com/connect-raspberry-pi-and-arduino-usb-cable/
import serial
import util

arduino = serial.Serial('/dev/ttyACM0', 9600)
util.Messages.Terminal.init
arduino.write('Hello from Raspberry Pi!'.encode())

# 1. ui k bo skos przgan da se ne vid pac oz da se ne more exitat (plus ma gumbke za izbiro vrat in pol odpre novo okno za opravljanje vrat),
# 2. nek fail-safe k se sproz ce se zapre ta program (aka se ne backproces k checka ce ta program deluje al ne (aka bash shit )) -> sproz da se al restarta program al pa sam ugasne,
# 3. funkcija k bo tejkala care za predvajanje videa (ce se prtisne gumb pr XOR vratih da pol predvaja npr: XOR.mp4 na loopu za tko idk x sekund; pol pa se vrne nazaj na prvortn ui),
# 4. funkcija k bo komunicirala z arduinotom (če se tm zazna da se ksn gumb prtisne da se to poročin in posledično predvaja simulacija)