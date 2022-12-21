#!/usr/bin/env python3
from pymongo import MongoClient
"""
Python script that provides some stats about Nginx logs stored in MongoDB:
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["logs"]
    coll = db["nginx"]

    # Obtiene el número total de documentos en la colección
    total_count = coll.count_documents({})
    print(f"{total_count} logs")

    # Imprime el número de documentos para cada método HTTP
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("\tMethods:")
    for method in methods:
        count = coll.count_documents({"method": method})
        print(f"\t\t{count}\t{method}")

    # Imprime el número de documentos con método=GET y path=/status
    count = coll.count_documents({"method": "GET", "path": "/status"})
    print(f"\t\t{count}\tGET /status")
