#!/usr/bin/env python3
"""
Hypermedia pagination that resists deletion
"""

import csv
import math
from typing import List, Dict


class Server:
    """popular baby name database can be paginated using a server class.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """stored dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed from 0 to the sorting position
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
        returns dictionary containing two integer argument
        the subsequent key-value pairings:
            index: index of the current page first item
            next_index: index of following page first item
            page_size: the size of the page as it is now
            data: page of dataset
        Args:
            index(int): the first required index
            page_size(int): number of records per page
        """
        dataset = self.indexed_dataset()
        data_length = len(dataset)
        assert 0 <= index < data_length
        response = {}
        data = []
        response['index'] = index
        for i in range(page_size):
            while True:
                curr = dataset.get(index)
                index += 1
                if curr is not None:
                    break
            data.append(curr)

        response['data'] = data
        response['page_size'] = len(data)
        if dataset.get(index):
            response['next_index'] = index
        else:
            response['next_index'] = None
        return response
