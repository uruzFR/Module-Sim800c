import serial
import time

# Connection with the serial port
ser = serial.Serial('/dev/ttyUSB0', 115200)

# Wait for the SIM800C module to be ready
time.sleep(2)

# Configure text mode for SMS
ser.write('AT+CMGF=1\r\n'.encode())
response = ser.readline()
print(response)

# Configure the SMS message format (17: UCS2, 167: 16-bit, 0: Normal message, 8: Disable delivery report)
ser.write(b'AT+CSMP=17,167,0,8\r\n')
response = ser.readline()
print(response)

# Set the recipient phone number
phone_number = '+1234567890'

# Set the message content
message = 'Hello, world!'

# Send the SMS
ser.write('AT+CMGS="{}"\r\n'.format(phone_number).encode())
response = ser.readline()
print(response)
ser.write(message.encode())
ser.write(bytes([26]))
response = ser.readline()
print(response)

# Close the serial connection
ser.close()

