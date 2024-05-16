from opensearchpy import OpenSearch
from opensearch_dsl import Search
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
                "message": "hello!"
            }
        }
    }
)

# Iterar sobre los resultados
for hit in response['hits']['hits']:
    print(hit)

