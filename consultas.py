from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from opensearchpy import OpenSearch

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

# Crear una consulta de búsqueda
s = Search(using=opensearch_client, index='syslog') \
   .query('match', message='hello!')

# Ejecutar la consulta
response = s.execute()

# Iterar sobre los resultados
for hit in response:
    print(hit)

