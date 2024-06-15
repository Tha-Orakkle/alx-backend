#!/usr/bin/env python3
"""
BasicCache Module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache Class: Inherits from BasicCaching
    """

    def put(self, key, item):
        """Assigns a new key and item to the self.cache_data
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Gets the value of teh given key
        """
        return self.cache_data.get(key, None)
