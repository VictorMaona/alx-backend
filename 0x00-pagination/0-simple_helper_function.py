#!/usr/bin/env python3
"""
includes the index_range helper function definition.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two with the start and end indexes
    corresponding to range of indexes to return in list for certain
    pagination parameters, given two integer arguments.
    Args:
        page (int): page number return (pages are 1-indexed)
        page_size (int): items per page
    Return:
        tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
