import socket
import string
import led_on as on
import led_off as off
import flash
import os

host = 'localhost'   
port = 10500         

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

data = ""
while True:

    while (string.find(data, "\n.") == -1):
        data = data + sock.recv(1024)

    strTemp = ""
    for line in data.split('\n'):
        index = line.find('WORD="')
        
        if index != -1:
            line = line[index + 6:line.find('"', index + 6)]
            if line != "[s]" :
                strTemp = strTemp + line

    print(":" + strTemp)
    if strTemp == "つけて":  
	on.main()	
    if strTemp == "けして":  
	off.main()
    if strTemp == "てんめつ":
        flash.main()
    data = ""
