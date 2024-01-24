#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
import uuid
from typing import Union, Optional, Callable


class Cache():
    """ doc """

    def __init__(self):
        """ init """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            store the input data in Redis using the random key
            and return the key.
        """
        id = str(uuid.uuid4())
        self._redis.set(id, data)

        return (id)

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str,
                                                                    int,
                                                                    None]:
        """
            take a key string argument
            and an optional Callable argument named fn.
            This callable will be used to convert
            the data back to the desired format.
        """

        data = self._redis.get(key)

        if data is None:
            return None

        if fn is not None:
            return fn(data)

        return data

    def get_str(self, key: str) -> str:
        """ get the string representation from the self.get method """
        data = self.get(key,
                        lambda x: x.decode('utf-8')
                        if isinstance(x, bytes)
                        else str(x))
        return str(data)

    def get_int(self, key: str) -> Union[int, None]:
        """ get the integer representation from the self.get method """
        data = self.get(key,
                        lambda x: int(x) if x.isdigit() else None)

        return data
