#!/usr/bin/env python3
import uuid
from typing import Union
import redis
"""
Writing strings to Redis
"""


class Cache:
    """ Stores the history of inputs and outputs for a particular
    function
    """
    def __init__(self):
        """ Defining the constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ method take a data and returns a string """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
