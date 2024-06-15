#!/usr/bin/env python3
"""
FIFO Caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching Class"""
    def __init__(self):
        """initialises"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the Cache using the
        FIFO Replacement approach"""
        if not key or not item:
            return
        if key in self.cache_data.keys():
            self.cache_data.pop(key)
            self.cache_data[key] = item
            return
        if len(self.cache_data) == self.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print("DISCARD: {}".format(first_key))
            self.cache_data.pop(first_key)
        self.cache_data[key] = item

    def get(self, key):
        """Returns the value of a key from the cache"""
        return self.cache_data.get(key, None)
