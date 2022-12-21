#!/usr/bin/env python3
"""
Python function that returns the list of school having a specific topic:
"""


def schools_by_topic(mongo_collection, topic):
    """
    Gets the documents in the collection that have the specified topic
    """
    doc = mongo_collection.find({"topics": "topic"})
    return list(doc)
