import sorting_algorithm.basic_helpers as hf
import sorting_algorithm.sorting_test as data
import sorting_algorithm.elementory_sorting as sorting


# Quicksort
# is a divide-and-conquer method for sorting.
# It works by partitioning an array into two parts, then sorting the parts independently.


def partition_inplace(alist, lo, hi):
    """
    First, we arbitrarily choose a[lo] to be the partitioning item—the one that will go into its final position.
    Next, we scan from the left end of the array until we find an entry that is greater than (or equal to) the
    partitioning item, and we scan from the right end of the array until we find an entry less than (or equal to)
    the partitioning item.
    :param alist: list
    :param lo: start index, including
    :param hi: end index, including
    :return: the position/index of the partition item
    """

    if (hi - lo) < 1:
        return lo

    p_item = alist[lo]

    i, j = lo + 1, hi

    while i < j:
        while hf.less_than_or_equal(alist[i], p_item) and i < j:
            i += 1
        while hf.less_than(p_item, alist[j]) and i < j:
            j -= 1

        hf.exch(alist, i, j)

    hf.exch(alist, lo, i - 1)
    return i - 1


def quicksort(alist, lo, hi):
    """
    Improved implementation.
    Use in-place partition.
    :param alist: list
    :param lo: including
    :param hi: including
    :return: boolean, input list sorted
    """
    if hi <= lo:
        return
    p_index = partition_inplace(alist, lo, hi)
    quicksort(alist, lo, p_index-1)
    quicksort(alist, p_index+1, hi)
    return True


def simple_quicksort(alist):
    """
    Simple implementation.
    :param alist: list
    :return: sorted list
    """
    if len(alist) <= 1:
        return alist
    p_item = alist[0]
    smaller_list = [a for a in alist[1:] if a <= p_item]
    larger_list = [b for b in alist[1:] if b > p_item]

    return simple_quicksort(smaller_list) + [p_item] + simple_quicksort(larger_list)


# testing section

# print(data.TEST_A)
# print('========')
# print(partition_inplace(data.TEST_A, 0, len(data.TEST_A) - 1))

# aa = [2, 1]
# print(partition_inplace(aa, 0, len(aa) - 1))
# quicksort(data.TEST_A, 0, len(data.TEST_A)-1)
# print(data.TEST_A)

# print(simple_quicksort(data.TEST_A))
