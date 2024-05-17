from opensearchpy import OpenSearch
from opensearch_dsl import Search
import json

# Configurar la conexión a OpenSearch
host = "192.168.104.41"
#host = 'https://localhost'
port= 9200
auth = ('admin', 'admin')

# Config del OpenSearch
opensearch_client = OpenSearch(
    hosts = [{'host': host, 'port': port}],
    http_auth = auth,
    use_ssl = True,
    verify_certs = False,
    ssl_assert_hostname = False,
    ssl_show_warn = False  
)

# Realizar una consulta de búsqueda
response = opensearch_client.search(
    index='syslog',
    body={
        "query": {
            "match": {
                "message": "Linux"
            }
        }
    }
)

# Iterar sobre los resultados
# Iterar sobre los resultados
#for hit in response['hits']['hits']:
#    print(hit)# Iterar sobre los resultados
#for hit in response['hits']['hits']:
 #   print(hit['_source']['host'])

# Iterar sobre los resultados y estructurar la salida en formato JSON
resultados = []
for hit in response['hits']['hits']:
    resultados.append(hit)

# Imprimir los resultados en formato JSON
print(json.dumps(resultados, indent=2))

# Escribir los resultados en un archivo JSON
with open('resultados.json', 'w') as f:
    json.dump(resultados, f, indent=2)
