#!/usr/bin/env python3
"""
Python function that changes all topics of a school document based on the name:
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the document with the specified name and sets the topic list
    """

    result = mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": "topics"}})
    """ Returns the number of updated documents """
    return result.modified_count
