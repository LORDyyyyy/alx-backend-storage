#!/usr/bin/env python3
""" insert """


def insert_school(mongo_collection, **kwargs):
    """ doc """

    x = mongo_collection.insert_one(kwargs)

    return (x.inserted_id)
