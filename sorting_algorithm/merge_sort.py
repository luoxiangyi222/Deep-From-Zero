
import sorting_algorithm.compare_helpers as helpers
import sorting_algorithm.testing_data as data
import sorting_algorithm.elementory_sorting as sorting
import math


### merge sort


# combining two ordered arrays to make one larger ordered array.
# This operation immediately lends itself to a simple recursive sort method known as mergesort:
# to sort an array, divide it into two halves, sort the two halves (recursively), and then merge the results.


def merge_v1(lista, listb):
    """
    Assume the given lists are sorted already.
    This version create new list to store result.
    :param lista:
    :param listb:
    :return:
    """
    temp_list = []

    ia, ib = 0, 0

    while ia < len(lista) and ib < len(listb):
        if helpers.less_than(lista[ia], listb[ib]):
            temp_list.append(lista[ia])
            ia += 1
        else:
            temp_list.append(listb[ib])
            ib += 1

    if ia >= len(lista) and ib < len(listb):
        temp_list.extend(listb[ib:])
    if ib >= len(listb) and ia < len(lista):
        temp_list.extend(lista[ia:])

    return temp_list


def merge_in_place(alist: list, lo: int, mid: int, hi: int):
    """

    :param alist:
    :param lo:
    :param mid:
    :param hi:
    :return:
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


def merge_sort_top_down(alist):
    """

    :param alist:
    :return:
    """
    if len(alist) <= 1:
        return alist

    N = len(alist)
    mid_point = int(N / 2)

    # sort sub list
    left_list = sorting.insertion_sort(alist[:mid_point])
    right_list = sorting.insertion_sort(alist[mid_point:])

    # recursion
    left_sorted = merge_sort_top_down(left_list)
    right_sorted = merge_sort_top_down(right_list)

    return merge_v1(left_sorted, right_sorted)


def merge_sort_bottom_up(alist):
    """

    :param alist:
    :return:
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


print(data.TEST_A)

la = [1, 3, 5, 2, 4, 6, 10]


print(merge_in_place(la, 0, 2, 6))
print(merge_sort_top_down(data.TEST_A))
print(merge_sort_bottom_up(data.TEST_A))
