"""
module: k_the_largest
create a function k_the_largest
"""


def k_the_largest(array, k):
    """
    function: k_the_largest
    :param array: an array of numbers
    :param k: k-th the biggest element
    :return: (k-th element, position(index))
    """
    if k <= 0 or k > len(array):
        return None

    array_new = list(array)
    n = len(array_new)
    for i in range(n):
        for j in range(0, n-i-1):
            if array_new[j] > array_new[j+1]:
                array_new[j], array_new[j+1] = array_new[j+1], array_new[j]
    kth_largest_element = array_new[-k]
    index = array.index(kth_largest_element)
    return kth_largest_element, index
