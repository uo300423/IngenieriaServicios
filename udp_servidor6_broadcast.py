import random
from sys import argv
import socket



# crear socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) #broadcast

if len(argv) < 3:
    puerto = 12345
else:
    puerto = int(argv[2])

s.bind(("", puerto) )

print(f"Servidor escuchando en el puerto {puerto}")

while True:
    linea = " "
    datos, origen = s.recvfrom(1024)

    mensaje_recibido = datos.decode("utf-8")

    print("Mensaje recibido: ", datos)

    if datos == "BUSCANDO HOLA":
        linea = "IMPLEMENTO HOLA"
        
    if datos == "HOLA":
        linea = "HOLA IP: {origen[0]}"
        
    confirmacion = s.sendto(linea.encode(), origen)
        

