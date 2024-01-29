#!/usr/bin/env python3
"""
This module provides a `Server` class for paginating a database of popular
baby names. It includes methods to retrieve a cached dataset, calculate
index ranges for pagination, and get items for a specific page.
"""
import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize Server instance with a cached dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset, loading it from the CSV file if not
           already loaded.
        Returns:
            List[List]: The dataset as a list of lists.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """Calculate start and end index range for a `page`, with `page_size`.
        Args:
            page (int): Page number.
            page_size (int): Number of items per page.
        Returns:
            Tuple[int, int]: A tuple representing the start and end index
            range.
        """
        nextPageStartIndex = page * page_size
        return nextPageStartIndex - page_size, nextPageStartIndex

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get items for the given page number.
        Args:
            page (int): Page number.
            page_size (int): Number of items per page.
        Returns:
            List[List]: A list of rows if inputs are within range, otherwise an
            empty list.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        startIndex, endIndex = self.index_range(page, page_size)
        return self.dataset()[startIndex:endIndex]
