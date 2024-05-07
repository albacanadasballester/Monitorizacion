import socket
import requests

# Dirección IP y puerto del clúster de OpenSearch
opensearch_ip = '192.168.104.41'
opensearch_port = 5601

# URL del endpoint en OpenSearch para enviar los datos
url = f'http://{opensearch_ip}:{opensearch_port}/nombre_de_indice/_doc'

# Abre el archivo en modo lectura
with open('Linux.log', 'r') as archivo:
    # Lee las primeras 10 líneas del archivo
    lineas = archivo.readlines()[:10]

# Itera sobre cada línea y envíala a OpenSearch
for linea in lineas:
    # Crea el cuerpo de la solicitud con el contenido de la línea
    data = {'linea': linea.strip()}  # Se debe ajustar al formato de tu índice en OpenSearch

    # Realiza la solicitud POST a OpenSearch
    response = requests.post(url, json=data)

    # Verifica el código de estado de la respuesta
    if response.status_code == 201:
        print("Documento enviado exitosamente a OpenSearch.")
    else:
        print(f"Error al enviar el documento a OpenSearch. Código de estado: {response.status_code}")
