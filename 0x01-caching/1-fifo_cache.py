#!/usr/bin/env python3
""" BaseCaching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO caching system is defined by FIFOCache
    """

    def __init__(self):
        """
        The init function from parent to initialize the class
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Keep key-value pair cached
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))
                del self.cache_data[self.order[0]]
                del self.order[0]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return None or the value associated with the supplied key
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
