"""
Module implements the Bubble sort algorithm with the following features:
 - We can sort any nested data-type by passing data and a function containing the identifier.
 - Performs the sorting in both ascending/descending order.
 - Can be customized or extended for different data-structure.
 - Default implementation does not allocate extra memory.
"""
from the_python_algorithm.sorting.exceptions import (
    SortingFilterFunctionException, IncorrectSortingDataException, BubbleSortGenericException)


class BubbleSort:
    """
    Implementation of Bubble sort Algorithm.
    """

    def __init__(self, func=lambda x: x):
        self._func = func

    def __call__(self, data_list, asc=True, func=None):
        self.bubble_sort(data_list, asc=True, func=func)

    def bubble_sort(self, data_list, asc=True, func=None):
        """
        Description: A function that performs the sorting operation for the
        Parameters:
            data_list:
            asc:
            func: A function that
        Returns: A modified list
        """
        if not func or not self._func:
            raise SortingFilterFunctionException()

        if not data_list:
            raise IncorrectSortingDataException()

        _func = func or self._func
        try:
            for i in range(1, len(data_list)):
                for j in range(0, len(data_list) - i):
                    if asc:
                        _query = _func(data_list[j]) > _func(data_list[j + 1])
                    else:
                        _query = _func(data_list[j]) < _func(data_list[j + 1])

                    if _query:
                        data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
            return data_list
        except Exception as e:
            raise BubbleSortGenericException(e)


bs = BubbleSort()
