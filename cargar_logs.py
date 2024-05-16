<<<<<<< HEAD
import socket
import requests

# Dirección IP y puerto del clúster de OpenSearch
opensearch_ip = '192.168.104.41'
opensearch_port = 5013

# URL del endpoint en OpenSearch para enviar los datos
url = f'http://{opensearch_ip}:{opensearch_port}/nombre_de_indice/_doc'

# Abre el archivo en modo lectura
with open('Linux.log', 'r',encoding='iso-8859-1') as archivo:
    # Lee las primeras 10 líneas del archivo
    lineas = archivo.readlines()[:10]
=======
import socket 
UDP_IP = "192.168.104.41"
UDP_PORT = 5013

# Abre el archivo en modo lectura
with open('muestra.log', 'r',encoding='iso-8859-1') as archivo:
    lineas = archivo.readlines()

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

>>>>>>> main

# Itera sobre cada línea y envíala a OpenSearch
for linea in lineas:
    print(f'voy a insertar la linea {linea}')
    mensaje = linea.encode() #cambiar la codificacion
    sock.sendto(mensaje, (UDP_IP, UDP_PORT))
