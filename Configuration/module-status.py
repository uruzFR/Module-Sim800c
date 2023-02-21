import serial

# Open a serial connection to the USB port where the SIM800C module is connected
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

# Send the AT+CSCA? command to get the SMS center number
command = "AT+CSCA=?\r\n"
command_bytes = command.encode()
ser.write(command_bytes)
response = ser.read(1024)
print(response)

# Send the AT command to test the connection to the SIM800C module
command = "AT\r\n"
command_bytes = command.encode()
ser.write(command_bytes)
response = ser.read(1024)
print(response)

# Send the AT+CPIN? command to check if a SIM card is inserted and unlocked
command = "AT+CPIN?\r\n"
command_bytes = command.encode()
ser.write(command_bytes)
response = ser.read(1024)
print(response)

# Send the AT+COPS? command to check the network operator the SIM800C module is registered to
command = "AT+COPS?\r\n"
command_bytes = command.encode()
ser.write(command_bytes)
response = ser.read(1024)
print(response)

# Send the AT+CFUN? command to check the functionality level of the SIM800C module
command = "AT+CFUN?\r\n"
command_bytes = command.encode()
ser.write(command_bytes)
response = ser.read(1024)
print(response)

# Send the ATE0 command to disable verbal error messages
command = "ATE0\r\n"
command_bytes = command.encode()
ser.write(command_bytes)
response = ser.read(1024)
print(response)

# Send the AT+CSQ command to check the signal quality of the SIM800C module
command = "AT+CSQ\r\n"
command_bytes = command.encode()
ser.write(command_bytes)
response = ser.read(1024)
print(response)

# Send the AT+CGMR command to check the firmware version of the SIM800C module
command = "AT+CGMR\r\n"
command_bytes = command.encode()
ser.write(command_bytes)
response = ser.read(1024)
print(response)

# Send the AT+CREG? command to check the registration status on the network of the SIM800C module
command = "AT+CREG?\r\n"
command_bytes = command.encode()
ser.write(command_bytes)
response = ser.read(1024)
print(response)

# Send the AT+CGATT? command to check if the SIM800C module is attached or detached from the mobile network
command = "AT+CGATT?\r\n"
command_bytes = command.encode()
ser.write(command_bytes)
response = ser.read(1024)
print(response)

# Configure SMS settings
command = "AT+CSMP?\r\n"
command_bytes = command.encode()
ser.write(command_bytes)
response = ser.read(1024)
print(response)

# Close the serial connection
ser.close()

