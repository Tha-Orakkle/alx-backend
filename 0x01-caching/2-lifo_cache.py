#!/usr/bin/env python3
"""
LIFO Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Caching Class"""
    def __init__(self):
        """initialises"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the Cache using the
        LIFO Replacement approach"""
        if not key or not item:
            return
        if key in self.cache_data.keys():
            self.cache_data.pop(key)
            self.cache_data[key] = item
            return
        if len(self.cache_data) == self.MAX_ITEMS:
            last_key = self.cache_data.popitem()[0]
            print("DISCARD: {}".format(last_key))
        self.cache_data[key] = item

    def get(self, key):
        """Returns the value of a key from the cache"""
        return self.cache_data.get(key, None)
