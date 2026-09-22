import socket
from sys import argv

host = "localhost"
puerto = 9999

contador = 1

if len(argv) < 3 :
    print("Uso: python udp_cliente1.py host port")
    exit(1)
else :
    host = argv[1]
    puerto = int(argv[2])

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
linea = ""

while linea != "FIN":
    linea = input('Ingrese un mensaje (o "FIN" para terminar):')

    mandar = str(contador) + linea

    cliente.sendto(mandar.encode(), (host, puerto))

    contador+=1

cliente.close()
