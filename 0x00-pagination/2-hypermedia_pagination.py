#!/usr/bin/env python3
"""
Hypermedia Pagination
"""
import csv
from math import ceil
from typing import Any, Dict, List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Takes 2 int args and returns a list containing the
        required data from a dataset"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        self.dataset()
        if self.__dataset is None:
            return []

        range = index_range(page, page_size)
        return self.__dataset[range[0]: range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Returns dictionary that contains information about dataset:
        * page_size: the length of the returned dataset page
        * page: the current page number
        * data: the dataset page
        * next_page: number of the next page, None if no next page
        * prev_page: number of the previous page, None if no prev page
        * total_pages: the total number of pages in the dataset as an integer
        """
        data: List[List] = self.get_page(page, page_size)
        total_pages = ceil(len(self.dataset()) / page_size)
        next_page = (page + 1) if page < total_pages else None
        prev_page = (page - 1) if page > 1 else None
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
