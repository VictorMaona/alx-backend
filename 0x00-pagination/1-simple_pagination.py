#!/usr/bin/env python3
"""
Defines class server for paginating baby name database
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    tuple of size two with the start and end indexes
    containing start and index corresponds to range of
    indexes to return list for pagination parameters
    Args:
        page (int): number to return (pages are 1-indexed)
        page_size (int): number of items page
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
        """The Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        integer argument and return requested page frm dataset
        Args:
            page (int): page number must be positive integer
            page_size (int): number of records page must be a ve integer
        Return:
            lists containing required data from dataset
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
