#!/usr/bin/env python3
""" find all """


def list_all(mongo_collection):
    """ doc """

    if mongo_collection is None:
        return []

    return mongo_collection.find()
