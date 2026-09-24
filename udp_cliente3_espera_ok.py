import socket
from sys import argv

host = "localhost"
puerto = 9999

contador = 1

def timeout(s):
    s.settimeout(0.1)
    try:
        datagrama, origen = s.recvfrom(1024) # Tamaño máximo a recibir
        datagrama = datagrama.decode("utf8")
        if datagrama=="OK":
            print("Recibida confirmación")
        else:
            print("Recibido datagrama no esperado")
    except socket.timeout:
        print("ERROR. El datagrama de confirmación no llega")
    except:    # Otras posibles excepciones dejamos que las maneje el usuario
        raise

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

    timeout(cliente)

    contador+=1

cliente.close()
