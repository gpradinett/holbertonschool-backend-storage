#!/usr/bin/env python3
"""
Python function that changes all topics of a school document based on the name:
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the document with the specified name and sets the topic list
    """

    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
