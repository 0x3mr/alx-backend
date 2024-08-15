import csv
import math
from typing import List, Tuple
"""
Adds `get_page` method to `Server` class
"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    A function named index_range that takes two integer arguments page and page_size.

    The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end

class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Returns a list of rows from the dataset that correspond to the given page and page_size. """
        assert isinstance(page, int) and page > 0,
        assert isinstance(page_size, int) and page_size > 0,

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

if __name__ == "__main__":
    server = Server()

    try:
        should_err = server.get_page(-10, 2)
    except AssertionError:
        print("AssertionError raised with negative values")

    try:
        should_err = server.get_page(0, 0)
    except AssertionError:
        print("AssertionError raised with 0")

    try:
        should_err = server.get_page(2, 'Bob')
    except AssertionError:
        print("AssertionError raised when page and/or page_size are not ints")

    print(server.get_page(1, 3))
    print(server.get_page(3, 2))
    print(server.get_page(3000, 100))