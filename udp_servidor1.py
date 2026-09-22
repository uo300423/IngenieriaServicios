from sys import argv
import socket

# crear socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

puerto = 9999

servidor.bind(("", puerto) )

print(f"Servidor escuchando en el puerto {puerto}")

while True:
    datos, origen = servidor.recvfrom(1024)

    mensaje = datos.decode("utf-8")

    print(f"Origen: {origen}")

    print(f"Mensaje: {mensaje}")

