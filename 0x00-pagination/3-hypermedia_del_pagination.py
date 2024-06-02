#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Any, Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
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
        Returns a dictionary that contains data from a dataset using
        the given index as the start point. Dictionary will contain
        * index: index of start point and first item on the page
        * next_index: index of the next page
        * page_size: number of item on a page
        * data: data of exah item
        """

        indexed_data = self.indexed_dataset()
        assert type(index) is int and index < len(indexed_data)

        count = 0
        cur_idx: int = index
        data: List[Any] = []

        while count < page_size and cur_idx < len(indexed_data):
            sub_data = indexed_data.get(cur_idx)
            if sub_data:
                data.append(sub_data)
                count += 1
            cur_idx += 1

        next_idx = None
        while cur_idx < len(indexed_data):
            sub_data = indexed_data.get(cur_idx)
            if sub_data:
                next_idx = cur_idx
                break
            cur_idx += 1

        return {
            'index': index,
            'next_index': next_idx,
            'page_size': page_size,
            'data': data
        }
