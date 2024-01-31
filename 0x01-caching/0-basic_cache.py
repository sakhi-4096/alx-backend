#!/usr/bin/python3
"""Basic Cache Implementation Class"""
from base_caching import BaseCaching
from typing import Optional, Any, Dict

class BasicCache(BaseCaching):
    """
    A basic cache implementation class.
    Attributes:
        MAX_ITEMS: The maximum number of items that can be stored in the cache.
    """

    def put(self, key: str, item: Any) -> None:
        """
        Add an item to the cache.

        Args:
            key (str): The key associated with the item.
            item (Any): The item to be stored in the cache.
        Returns:
            None
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key: str) -> Optional[Any]:
        """
        Get an item from the cache by key.

        Args:
            key (str): The key associated with the item to be retrieved.
        Returns:
            Any: The item corresponding to the key if found, otherwise None.
        """
        return self.cache_data.get(key, None)
