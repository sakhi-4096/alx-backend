#!/usr/bin/env python3
"""
This module extends the `Server` class with a method named `get_hyper`,
which provides advanced pagination information along with the paginated data.
"""
import csv
from typing import Dict, List, Tuple, Union


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

    def get_hyper(self, page: int,
                  page_size: int) -> Dict[str, Union[int, List[List], None]]:
        """
        Get paginated data along with advanced pagination information.
        Args:
            page (int): Page number.
            page_size (int): Number of items per page.
        Returns:
            Dict[str, Union[int, List[List], None]]: A dictionary containing:
                - page_size: Number of items on the current page.
                - page: Current page number.
                - data: Paginated data for the current page.
                - next_page: Next page number (None if on the last page).
                - prev_page: Previous page number (None if on the first page).
                - total_pages: Total number of pages.
        """
        data = self.get_page(page, page_size)
        total_rows = len(self.dataset())
        prev_page = page - 1 if page > 1 else None
        next_page = (page + 1 if self.index_range(page, page_size)[1]
                     < total_rows else None)
        total_pages = (total_rows // page_size +
                       (1 if total_rows % page_size != 0 else 0))
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
