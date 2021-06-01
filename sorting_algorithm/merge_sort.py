
import sorting_algorithm.compare_helpers as helpers
import sorting_algorithm.testing_data as data
import sorting_algorithm.elementory_sorting as sorting
import math

### merge sort
# combining two ordered arrays to make one larger ordered array.
# This operation immediately lends itself to a simple recursive sort method known as mergesort:
# to sort an array, divide it into two halves, sort the two halves (recursively), and then merge the results.

def merge(lista, listb):
    """
    Assume the given lists are sorted already.
    :param lista:
    :param listb:
    :return:
    """
    temp_list = []

    ia, ib = 0, 0
    while ia < len(lista) or ib < len(listb):
        pass


def merge_sort_v1(alist):
    """
    Top down method.
    :param alist:
    :return:
    """
    N = len(alist)
    mid_point = int(N / 2)

    left_list = alist[:mid_point]
    right_list = alist[mid_point:]
