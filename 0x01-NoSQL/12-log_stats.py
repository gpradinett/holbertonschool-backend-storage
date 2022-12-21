#!/usr/bin/env python3
from pymongo import MongoClient
"""
 Python script that provides some stats about Nginx logs stored in MongoDB:
"""


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    number_logs = collection.count_documents({})
    print("""{} logs
Methods:""".format(number_logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        logs = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, logs))

    pathlogs = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(pathlogs))

    print("IPs:")
    ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    for ip in ips:
        print("\t{}: {}".format(ip["_id"], ip["count"]))
