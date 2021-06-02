

def less_than(n1, n2):
    return n1 < n2


def less_than_or_equal(n1, n2):
    return n1 <= n2


def exch(alist, i, j):

    if i >= len(alist) or j >= len(alist):
        raise IndexError

    temp = alist[i]
    alist[i] = alist[j]
    alist[j] = temp
    return True
