import serial

# Open the serial port using the appropriate port address and baud rate
ser = serial.Serial('/dev/ttyUSB0', 115200)

# Send the AT+CPIN command followed by your SIM card's PIN code to unlock the SIM card
pin = '1234'
ser.write(f'AT+CPIN={pin}\r\n'.encode())

# Get the response from the module and display it
response = ser.readline()
print(response.decode())

# Close the serial port
ser.close()

