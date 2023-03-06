# https://oscarliang.com/connect-raspberry-pi-and-arduino-usb-cable/
import serial
from util import Start


ser = serial.Serial('/dev/ttyUSB0', 9600)

#util.Messages.Terminal.init
ser.write('Hello from Raspberry Pi!'.encode())

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
    path = f"/home/pi/matura/anim/{select}.mp4" if select in gate_list else None
    #print(path)
    if path is not None: 
        os.system(f"vlc --play-and-exit {path}")
        print("sleeping...")
        time.sleep(10)
        print("awake")
#Start.init_check()

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
        
