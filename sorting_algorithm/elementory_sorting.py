
import sorting_algorithm.compare_helpers as helpers
import sorting_algorithm.testing_data as data
import math


def selection_sort(alist):
    """
    First, find the smallest item in the array, and exchange it with the first entry. Then, find the next smallest item
    and exchange it with the second entry. Continue in this way until the entire array is sorted. This method is called
    selection sort because it works by repeatedly selecting the smallest remaining item.
    :param alist:
    :return:
    """

    if not alist:
        return False

    for i in range(len(alist)):
        for j in range(i+1, len(alist)):
            if not helpers.less_than(alist[i], alist[j]):
                helpers.exch(alist, i, j)

    return True


def insertion_sort(alist):
    """
     The algorithm that people often use to sort bridge hands is to consider the cards one at a time, inserting each
     into its proper place among those already considered (keeping them sorted). In a computer implementation,
     we need to make space for the current item by moving larger items one position to the right,
     before inserting the current item into the vacated position.
    :param alist:
    :return:
    """

    if not alist:
        return False

    for i in range(1, len(alist)):
        for j in (range(i)):
            if helpers.less_than(alist[i], alist[j]):
                helpers.exch(alist, i, j)

    return True


def shell_sort(alist):
    """
    The idea is to rearrange the array to give it the property that taking every hth entry (starting anywhere) yields
    a sorted sequence. Such an array is said to be h-sorted

    Here, we use N / 2 for gap sequence.
    :param alist:
    :return:
    """
    if not alist:
        return False

    if len(alist) <= 1:
        return True

    N = len(alist)
    h = math.floor(N / 2)  # gap

    while h >= 1:
        # do h-sorting
        size = math.ceil(N / h)
        for g in range(h):  # each group
            for i in range(g + h, g + h * size, h):
                if i < N:
                    for j in range(g, i, h):
                        if helpers.less_than_or_equal(alist[i], alist[j]):
                            helpers.exch(alist, i, j)

        h = math.floor(h / 2)

    return True


print(data.TEST_A)
shell_sort(data.TEST_A)
print(data.TEST_A)

