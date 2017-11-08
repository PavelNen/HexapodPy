import serial
ser = serial.open('COM3', 115200, timeout=0)
var = raw_input("#0P2000 ")
ser.write(var)
