#!/usr/bin/env python3
"""
Main file
"""
import redis

# Cache = __import__('exercise').Cache

# cache = Cache()

# data = b"hello"
# key = cache.store(data)
# print(key)

local_redis = redis.Redis()
# print(local_redis.get(key))



# Cache = __import__('exercise').Cache

# cache = Cache()

# cache.store(b"first")
# print(cache.get(cache.store.__qualname__))

# cache.store(b"second")
# cache.store(b"third")
# print(cache.get(cache.store.__qualname__))


#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache
replay = __import__('exercise').replay

cache = Cache()

s1 = cache.store("first")
print(s1)
s2 = cache.store("secont")
print(s2)
s3 = cache.store("third")
print(s3)


inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

print(cache.store.__qualname__)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))

print('\n\n\n\n')

replay(cache.store)

print(cache.store.__qualname__)
print(local_redis.get(cache.store.__qualname__))
