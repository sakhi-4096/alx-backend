#!/usr/bin/python3
"""LFU Cache Replacement Implementation Class"""
from threading import RLock
from typing import Optional

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    An implementation of LFU (Least Frequently Used) Cache.

    Attributes:
        __stats (dict): A dictionary of cache keys for access count.
        __rlock (RLock): Lock accessed resources to prevent race conditions.
    """

    def __init__(self) -> None:
        """Instantiation method, sets instance attributes."""
        super().__init__()
        self.__stats = {}
        self.__rlock = RLock()

    def put(self, key: str, item: str) -> None:
        """
        Add an item to the cache.

        Args:
            key (str): The key associated with the item.
            item (str): The item to be stored in the cache.
        Returns:
            None
        """
        if key is not None and item is not None:
            key_out = self._balance(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if key_out is not None:
                print('DISCARD: {}'.format(key_out))

    def get(self, key: str) -> Optional[str]:
        """
        Get an item from the cache by key.

        Args:
            key (str): The key associated with the item to be retrieved.
        Returns:
            Optional[str]: The item corresponding to the key if found,
                           otherwise None.
        """
        with self.__rlock:
            value = self.cache_data.get(key, None)
            if key in self.__stats:
                self.__stats[key] += 1
        return value

    def _balance(self, key_in: str) -> Optional[str]:
        """
        Removes the earliest item from the cache at MAX size.

        Args:
            key_in (str): The key of the new item being added.
        Returns:
            Optional[str]: The key of the discarded item if the cache is at
                           max size, otherwise None.
        """
        key_out = None
        with self.__rlock:
            if key_in not in self.__stats:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    key_out = min(self.__stats, key=self.__stats.get)
                    self.cache_data.pop(key_out)
                    self.__stats.pop(key_out)
            self.__stats[key_in] = self.__stats.get(key_in, 0) + 1
        return key_out
