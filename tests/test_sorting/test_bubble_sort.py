import pytest

from the_python_algorithm.sorting.bubble_sort import bs
from .testdata import (
    dataset1, dataset2, dataset3)


@pytest.mark.parametrize(
    "test_input,asc,func,expected",
    [dataset1, dataset2, dataset3]
)
def test_bubble_sort(test_input, asc, func, expected):
    # To make sure intially values are not equal 
    assert test_input != expected
    
    #TODO: write a profiler class to evaluate the time and space complexity
    bs(test_input, asc, func) # Here we make sure that, we dont create a new variable, 
                              # rather we make the changes to the existing variable
                              
                              # TODO: create a utility that create a replica of the 
                              # exiting variable(can be of any datatype) and does not 
                              # modify the existing variable. Thus, it should take the 
                              # type of sorting method as input and returns the sorted list
                              # Very similar to the functionality of the sorted(), however, 
                              # an enhanced version of it
                              
    # Verify of the sorted list and the expected result are same or not
    assert test_input == expected
