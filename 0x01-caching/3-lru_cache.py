#!/usr/bin/env python3
"""
Least Recently Used (LRU) Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching Class"""
    def __init__(self):
        """initialises"""
        super().__init__()
        self.lru_list = []

    def put(self, key, item):
        """Adds an item to the Cache using the
        LRU Replacement approach"""
        if not key or not item:
            return None
        if key in self.cache_data.keys():
            self.cache_data[key] = item
            self.lru_list.remove(key)
            self.lru_list.append(key)
            return
        if len(self.cache_data) == self.MAX_ITEMS:
            lru_key = self.lru_list.pop(0)
            self.cache_data.pop(lru_key)
            print("DISCARD: {}".format(lru_key))
        self.cache_data[key] = item
        self.lru_list.append(key)

    def get(self, key):
        """Gets and Return the value of the key.
        Counts number of times an item in cache is used"""
        if not key or key not in self.cache_data.keys():
            return None
        self.lru_list.remove(key)
        self.lru_list.append(key)
        return self.cache_data[key]
