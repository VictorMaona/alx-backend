#!/usr/bin/env python3
"""
Defines class server for paginating baby name database that is popular.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two with the start and end indexes
    corresponding to the range of indexes to return in a list for certain
    pagination parameters, given two integer arguments
    Args:
        page (int): page to return (pages are 1-indexed)
        page_size (int): quantity of objects on a page
    Return:
        tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)


class Server:
    """server class that paginates list of well liked baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """stored dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        retrieves specified page from dataset after receiving two integer inputs
        Args:
            page (int): necessary page number ought to be integer that is positive
            page_size (int): Record page must be represented by a negative integer.
        Return:
            series of lists with the necessary dataset data
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        dataset = self.dataset()
        data_length = len(dataset)
        try:
            index = index_range(page, page_size)
            return dataset[index[0]:index[1]]
        except IndexError:
            return []
