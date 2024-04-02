#!/usr/bin/env python3
""" BaseCaching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Outlines a class for key-value pair caching of data.
    Methods:
        put(key, item) - store key-value pair
        get(key) - retrieve value associated with key
    """

    def __init__(self):
        """
        Parent class __init__ function to initialize the class
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Store key-value pair
        Args:
            Key
            Item
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value associated with the key.
        Return None if the key is None or does not exist
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
