#!/usr/bin/env python3
"""
includes class with methods for using CSV data to build basic pagination.
"""
import csv
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """server class that paginates a list of well liked baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        retrieves the dataset after reading from CSV file.
        Returns:
            List[List]: Dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def assert_positive_integer_type(value: int) -> None:
        """
        Declares value to be an integer that is positive.
        Args:
            value (int): The worth to be affirmed.
        """
        assert type(value) is int and value > 0

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        gives back a page from the dataset.
        Args:
            page (int): page number.
            page_size (int): page size.
        Returns:
            List[List]: page of dataset.
        """
        self.assert_positive_integer_type(page)
        self.assert_positive_integer_type(page_size)
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        try:
            data = dataset[start:end]
        except IndexError:
            data = []
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns page of dataset.
        Args:
            page (int): page number.
            page_size (int): page size.
        Returns:
            List[List]: page of dataset.
        """
        total_pages = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        info = {
            "page": page,
            "page_size": page_size if page_size <= len(data) else len(data),
            "total_pages": total_pages,
            "data": data,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page + 1 <= total_pages else None
        }
        return info
