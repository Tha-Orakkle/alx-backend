#!/usr/bin/env python3
"""
Most Recently Used (MRU) Caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU Caching Class"""
    def __init__(self):
        """initialises"""
        super().__init__()
        self.mru_list = []

    def put(self, key, item):
        """Adds an item to the Cache using the
        MRU Replacement approach"""
        if not key or not item:
            return None
        if key in self.cache_data.keys():
            self.cache_data[key] = item
            self.mru_list.remove(key)
            self.mru_list.append(key)
            return
        if len(self.cache_data) == self.MAX_ITEMS:
            mru_key = self.mru_list.pop(-1)
            self.cache_data.pop(mru_key)
            print("DISCARD: {}".format(mru_key))
        self.cache_data[key] = item
        self.mru_list.append(key)

    def get(self, key):
        """Gets and Return the value of the key.
        Counts number of times an item in cache is used"""
        if not key or key not in self.cache_data.keys():
            return None
        self.mru_list.remove(key)
        self.mru_list.append(key)
        return self.cache_data[key]
