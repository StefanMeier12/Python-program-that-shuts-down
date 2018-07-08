ip = raw_input("[[192,168,0,0],[192,168,255,255]]:")
NameError: name 'raw_input' is not defined

Program Design:

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = raw_input("[[192,168,0,0],[192,168,255,255]]:")
nachricht = raw_input("Nachricht: Jetzt ist Schlafenszeit")

s.sendto(nachricht, (ip, 1))
s.close()

if message == "shutdown" :
ser.close()
os.system("shutdown -h now")
sys.exit()
else: print("Gute Nacht")

