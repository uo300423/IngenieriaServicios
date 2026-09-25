import socket
from sys import argv

host = "localhost"
puerto = 12345


def timeout(s):
    s.settimeout(0.1)
    

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

#mandamos por broadcast
cliente.sendto("BUSCANDO HOLA".encode("utf-8"), ("192.168.11.255", puerto))

primera_ip = None
timeout(cliente)

while True:
    try:
        datagrama, origen = cliente.recvfrom(1024)
    except socket.timeout:
        break
    
    ip = origen[0] #cogemos primera IP que responda
    print("Servidor que primero ha respondido: " , ip)

    if primera_ip is None:
        primera_ip = ip
    
if ip is not None:
    cliente.sendto("HOLA".encode("utf-8"), (primera_ip, puerto))
    timeout(cliente)

    respuesta, origen = cliente.recvfrom(1024)
    print("Respuesta: ", respuesta)
    
