#!/usr/bin/env python3
"""
This module defines a `Server` class to paginate a database of popular
baby names. The pagination strategy is designed to handle cases where
rows are removed from the dataset between queries, ensuring users do not
miss items when changing pages.
"""

import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize Server instance with cached datasets."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Return the cached dataset, loading it from the CSV file if not
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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Return the dataset indexed by sorting position, starting at 0.

        Returns:
            Dict[int, List]: The dataset as a dictionary with index keys.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get paginated data with deletion-resilient hypermedia pagination.

        The goal is to handle cases where rows are removed from the dataset
        between queries,
        ensuring users do not miss items when changing pages.

        Args:
            index (int): Start index of the current page.
            page_size (int): Size of items required on the current page.

        Returns:
            Dict[int, int|List[List]|None]: A dictionary containing:
                - index: Start index of the current page.
                - data: Paginated data for the current page.
                - page_size: Number of items on the current page.
                - next_index: Start index of the next page (None if on the
                              last page).
        """
        focus = []
        dataset = self.indexed_dataset()
        index = 0 if index is None else index
        keys = sorted(dataset.keys())
        assert index >= 0 and index <= keys[-1]
        [focus.append(i)
         for i in keys if i >= index and len(focus) <= page_size]
        data = [dataset[v] for v in focus[:-1]]
        next_index = focus[-1] if len(focus) - page_size == 1 else None
        return {'index': index, 'data': data,
                'page_size': len(data), 'next_index': next_index}
