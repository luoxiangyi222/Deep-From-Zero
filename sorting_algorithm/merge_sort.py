
import sorting_algorithm.basic_helpers as helpers
import sorting_algorithm.sorting_test as data
import sorting_algorithm.elementory_sorting as sorting

# Merge sort
# Combining two ordered arrays to make one larger ordered array.
# This operation immediately lends itself to a simple recursive sort method known as mergesort:
# to sort an array, divide it into two halves, sort the two halves (recursively), and then merge the results.


def merge_v1(lista, listb):
    """
    Assume the given lists were sorted already.
    This version create new list to store result.
    :param lista: sorted list
    :param listb: sorted list
    :return: sorted list merged from list a and list b
    """
    temp_list = []

    ia, ib = 0, 0

    # when two pointers are inside arrays
    while ia < len(lista) and ib < len(listb):
        if helpers.less_than(lista[ia], listb[ib]):
            temp_list.append(lista[ia])
            ia += 1
        else:
            temp_list.append(listb[ib])
            ib += 1

    # Check if pointers hit the tail of array.
    if ia >= len(lista) and ib < len(listb):
        temp_list.extend(listb[ib:])
    if ib >= len(listb) and ia < len(lista):
        temp_list.extend(lista[ia:])

    return temp_list


def merge_in_place(alist: list, lo: int, mid: int, hi: int):
    """
    Assume the given sub lists were sorted.
    This version merge left and right parts in place.
    :param alist: list
    :param lo: low index
    :param mid: mid index separating left and right part, belongs to left part.
    :param hi: high index, belongs to right part
    :return: a whole sorted list
    """

    temp_list = alist.copy()

    i, j = lo, mid + 1

    for k in range(lo, hi+1):
        if i > mid:
            alist[k] = temp_list[j]
            j += 1
        elif j > hi:
            alist[k] = temp_list[i]
            i += 1
        elif helpers.less_than(temp_list[i], temp_list[j]):
            alist[k] = temp_list[i]
            i += 1
        else:
            alist[k] = temp_list[j]
            j += 1

    return alist


def merge_sort_top_down_v1(alist):
    """
    Divide and conquer. Top down method for merge sort.
    Each recursion requires a creation of new array.
    :param alist: list
    :return: sorted list.
    """
    if len(alist) <= 1:
        return alist

    N = len(alist)
    mid_point = int(N / 2)

    # sort sub list
    # insertion sort
    left_list = sorting.insertion_sort(alist[:mid_point])
    right_list = sorting.insertion_sort(alist[mid_point:])

    # recursion
    left_sorted = merge_sort_top_down_v1(left_list)
    right_sorted = merge_sort_top_down_v1(right_list)

    return merge_v1(left_sorted, right_sorted)


def merge_sort_top_down_inplace(alist):
    """
    Divide and conquer. Top down method for merge sort.
    Stave off creating new array and append elements to form result.
    :param alist: list
    :return: sorted list
    """
    if len(alist) <= 1:
        return alist

    N = len(alist)
    mid_point = int(N / 2)

    # sort
    alist[: mid_point+1] = sorting.insertion_sort(alist[: mid_point+1])
    alist[mid_point+1:] = sorting.insertion_sort(alist[mid_point+1:])

    # merge
    merge_in_place(alist, 0, mid_point, N-1)

    return alist


def merge_sort_bottom_up(alist):
    """
    Bottom up method, start with size 2, following 4, 8, ...
    :param alist: list
    :return: sorted list
    """
    N = len(alist)

    size = 2

    while size < 2*N:
        i = 0
        while i < N:
            alist[int(i):int(i+size)] = merge_v1(alist[i: int(i + size/2)], alist[int(i + size/2): i + size])
            i += size
        size *= 2
    return alist


# testing section
# print(data.TEST_A)
# print(merge_sort_top_down_inplace(data.TEST_A))
# print(merge_sort_bottom_up(data.TEST_A))
