import serial

# Open the serial connection to the USB port where the SIM800C module is connected
ser = serial.Serial('/dev/ttyUSB0', 115200)

# Send the command AT+CLIP=1 to enable caller identity notification
command = "AT+CLIP=1\r\n"
command_bytes = command.encode()
ser.write(command_bytes)
response = ser.read(1024)
print(response)

# Send the command ATD followed by the phone number to make a call
number = "0645123456"
command = f"ATD{number};\r\n"
command_bytes = command.encode()
ser.write(command_bytes)
response = ser.read(1024)
print(response)

# Close the serial connection
ser.close()

