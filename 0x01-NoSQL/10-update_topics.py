#!/usr/bin/env python3
""" update """


def update_topics(mongo_collection, name, topics):
    """ doc """

    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
