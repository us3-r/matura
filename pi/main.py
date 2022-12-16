# https://oscarliang.com/connect-raspberry-pi-and-arduino-usb-cable/
import serial
import util

arduino = serial.Serial('/dev/ttyACM0', 9600)
util.Messages.Terminal.init
arduino.write('Hello from Raspberry Pi!'.encode())