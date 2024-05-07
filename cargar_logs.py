import socket
UDP_IP = "10.88.0.4"
UDP_PORT = 5013

# Abre el archivo en modo lectura
with open('muestra.log', 'r',encoding='iso-8859-1') as archivo:
    # Lee las primeras 10 líneas del archivo
    lineas = archivo.readlines()

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP


# Itera sobre cada línea y envíala a OpenSearch
for linea in lineas:
    print(f'voy a enviar esta linea {linea}')
    mensaje = linea.encode() #cambiar la codificacion
    sock.sendto(mensaje, (UDP_IP, UDP_PORT))

