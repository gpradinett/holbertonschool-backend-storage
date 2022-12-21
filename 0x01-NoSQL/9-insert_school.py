#!/usr/bin/env python3
"""
Python function that inserts a new document in a collection based on kwargs:
"""

def insert_school(mongo_collection, **kwargs):
    """
    Create the document from the key-value arguments
    """
    doc = {}
    for key, value in kwargs.items():
        doc[key] = value
    """ Insert the document into the collection """
    result = mongo_collection.insert_one(doc)
    """ Returns the _id of the new document """
    return result.inserted_id
