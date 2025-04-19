from more_itertools import pairwise


def is_sorted_ascending(lst):
    return all(a <= b for a, b in pairwise(lst))
