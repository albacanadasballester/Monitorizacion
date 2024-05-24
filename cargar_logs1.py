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

# Abre el archivo en modo lectura
with open('Linux.log', 'r',encoding='iso-8859-1') as archivo:
    lineas = archivo.readlines()

# Itera sobre cada línea y envíala a OpenSearch
for linea in lineas:
    print(f'voy a insertar la linea {linea}')
    log_json = {
            "host":"localhost",
            "message" : linea.strip(),
            "client_addr": host
        
        }
    opensearch_client.index(index="syslog",body=log_json)
