import serial

serial = serial.Serial('COM5',1000000)
while True:
    data = serial.readline()
    print(data)

#cntrl+c to generate keyboard interuppt to break the loop. 



