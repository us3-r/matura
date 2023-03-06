# https://oscarliang.com/connect-raspberry-pi-and-arduino-usb-cable/
import serial
from util import Start


ser = serial.Serial('/dev/ttyUSB0', 9600)

#util.Messages.Terminal.init
video_running = False
current_video = ""

def get_video(select :str):
    import os
    global video_running
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
        video_running = True
        os.system(f"vlc --play-and-exit --fullscreen {path}")
        video_running = False

Start.init_check()

while True:
    if not video_running:
        if ser.in_waiting > 0:
            message = ser.readline().strip().decode('utf-8')  # read the message from serial
            pass_video = message
            import time
            ct =time.strftime("%H:%M")
            log_rep = f"[ at {ct} ]\nSerial data: {ser}\nDecoded message: {message}\n"
            with open("log.log", "a") as file:
                file.write(log_rep)
            if pass_video == current_video: pass
            else:
                current_video=pass_video
                get_video(message)
            #print(message)  # print the message to the console
            
        
