#!/usr/bin/env python3
"""
Write a Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Gets all documents in the collection
    """
    doc = mongo_collection.find()

    """ If there are no documents, it returns an empty list"""
    if doc == 0:
        return []

    """Create a list of documents"""
    doc_list = []
    for doc in doc:
        doc_list.append(doc)
        return doc_list
