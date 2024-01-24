#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
import uuid
from typing import Union


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
