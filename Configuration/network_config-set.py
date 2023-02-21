import serial

# Open the serial port using the appropriate port address and baud rate
ser = serial.Serial('/dev/ttyUSB0', 115200)

# Send the AT+COPS=0 command to automatically select the mobile network
ser.write(b'AT+COPS=0\r\n')

# Get the response from the module and display it
response = ser.readline()
print(response.decode())

# Close the serial port
ser.close()

