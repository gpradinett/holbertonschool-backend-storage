#!/usr/bin/env python3
"""Writing strings to Redis
"""
import redis
import uuid
from typing import Union, Callable, Any, Optional
from functools import wraps


def call_history(method: Callable) -> Callable:
    """Stores the history of inputs and outputs for a particular
    function
    """
    in_key = method.__qualname__ + ":inputs"
    out_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(in_key, str(args))
        res = method(self, *args)
        self._redis.rpush(out_key, str(res))
        return res
    return wrapper


def count_calls(method: Callable) -> Callable:
    """Counts how many times methods of the Cache class
    have been called.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, args):
        k = method(self, args)
        self._redis.incr(key)
        return k

    return wrapper


def replay(method: Callable):
    """Displays the history of calls of a particular function
    """
    client = redis.Redis()
    st_name = Cache.store.__qualname__

    inputs = client.lrange("{}:inputs".format(st_name), 0, -1)
    outputs = client.lrange("{}:outputs".format(st_name), 0, -1)

    print("{} was called {} times:".format(st_name,
          client.get(st_name).decode("utf-8")))
    for i, o in tuple(zip(inputs, outputs)):
        print("{}(*('{}',)) -> {}".format(st_name, i.decode("utf-8"),
              o.decode("utf-8")))


class Cache:
    """A redis cache class
    Args:
        _redis: private instance of the Redis client
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores input data in Redis using a random key
        """
        key = str(uuid.uuid1())
        self._redis.mset({key: data})
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Gets the value of a string and returns it converted to
        the right type
        """
        if fn:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)
