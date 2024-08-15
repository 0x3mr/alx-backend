#!/usr/bin/env python3
from typing import Tuple

""" Simple Helper Function """


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    A function named index_range that takes two integer arguments page and page_size.

    The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end