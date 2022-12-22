#!/usr/bin/env python3
import uuid
from typing import Union
import redis
"""
Writing strings to Redis
"""


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
    """ Stores the history of inputs and outputs for a particular
    function
    """
    def __init__(self):
        """ Defining the constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

	@call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ method take a data and returns a string """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
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
	
