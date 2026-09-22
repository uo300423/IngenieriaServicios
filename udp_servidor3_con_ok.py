import random
from sys import argv
import socket

# crear socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

puerto = 9999

servidor.bind(("", puerto) )

print(f"Servidor escuchando en el puerto {puerto}")

while True:
    datos, origen = servidor.recvfrom(1024)

    probabilidad = random.randint(0, 1)

    if probabilidad == 0:
        print("Simulando paquete perdido")
    else :
        mensaje = datos.decode("utf-8") 
        okey = "OK"
        confirmacion = servidor.sendto(okey.encode(), (origen, puerto))
        print(f"Origen: {origen}")
        print(f"Mensaje: {mensaje}")

