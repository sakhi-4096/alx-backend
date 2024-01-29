#!/usr/bin/env python3
"""
Defines a function named `index_range`.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters.

    Args:
        page (int): The current page.
        page_size (int): The amount of items in a page.
    Returns:
        tuple: A tuple of the start and end index for the given page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
