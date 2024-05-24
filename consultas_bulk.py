from opensearchpy import OpenSearch
from opensearch_dsl import Search
import os
from typing import Any
import json

def main()-> None:
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

    # check whether an index exists
    index_name = "syslog"
    if not opensearch_client.indices.exists(index_name):
        opensearch_client.indices.create(
                index_name,
                source ={
                    "host":"localhost",
                    "ident":"prueba",
                    "message":"insertar datos mediante bulk"
                    }
                )

    # index data
    data: Any = []
    for i in range(10):
        data.append({"index": {"_index": index_name, "_id": i}})
        data.append({"value": i,
                     "localhost":"alba",
                     "message":"insertar datos mediante bulk"
                     })
    

    rc = opensearch_client.bulk(data)  # pylint: disable=invalid-name
    if rc["errors"]:
        print("There were errors:")
        for item in rc["items"]:
            print(f"{item['index']['status']}: {item['index']['error']['type']}")
    else:
        print(f"Bulk-inserted {len(rc['items'])} items.")

    # delete index
    #opensearch_client.indices.delete(index=index_name)


if __name__ == "__main__":
    main()

