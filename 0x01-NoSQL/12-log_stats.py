#!/usr/bin/env python3
from pymongo import MongoClient
"""
 Python script that provides some stats about Nginx logs stored in MongoDB:
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    print("{} logs".format(collection.estimated_document_count()))
    print("Methods:")
    print("\tmethod GET: {}".format(collection.count_documents
                                    ({"method": "GET"})))
    print("\tmethod POST: {}".format(collection.count_documents
                                     ({"method": "POST"})))
    print("\tmethod PUT: {}".format(collection.count_documents
                                    ({"method": "PUT"})))
    print("\tmethod PATCH: {}".format(collection.count_documents
                                      ({"method": "PATCH"})))
    print("\tmethod DELETE: {}".format(collection.count_documents
                                       ({"method": "DELETE"})))
    print("{} status check".format(collection.count_documents
                                   ({"path": "/status"})))
