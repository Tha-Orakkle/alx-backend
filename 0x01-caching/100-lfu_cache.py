#!/usr/bin/env python3
"""
Least Frequently Used (LFU) Caching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU Caching Class"""
    def __init__(self):
        """initialises"""
        super().__init__()
        self.use_count = {}
        self.lru_list = []

    def put(self, key, item):
        """Adds an item to the Cache using the
        LRU Replacement approach"""
        if not key or not item:
            return
        if key in self.cache_data.keys():
            self.cache_data[key] = item
            self.use_count[key] += 1
            self.lru_list.remove(key)
            self.lru_list.append(key)
            return
        if len(self.cache_data) == self.MAX_ITEMS:
            lfu_keys = [k
                        for k in self.use_count.keys()
                        if self.use_count[k] == min(self.use_count.values())
                        ]
            if len(lfu_keys) == 1:
                lru_key = lfu_keys[0]
            elif len(lfu_keys) > 1:
                # find the lru from the lfu
                for x in self.lru_list:
                    if x in lfu_keys:
                        lru_key = x
                        break

            self.lru_list.remove(lru_key)
            self.cache_data.pop(lru_key)
            self.use_count.pop(lru_key)
            print("DISCARD: {}".format(lru_key))
        self.cache_data[key] = item
        self.use_count[key] = 1
        self.lru_list.append(key)

    def get(self, key):
        """Gets and Return the value of the key.
        Counts number of times an item in cache is used"""
        if not key or key not in self.cache_data.keys():
            return None
        self.use_count[key] += 1
        self.lru_list.remove(key)
        self.lru_list.append(key)
        return self.cache_data[key]
