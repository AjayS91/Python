# # Beginners mini challenge no. 8. Python version 2.7.

##############################################################
######### Published to Python Programming Society ############
#########              October 2014               ############
#########       Author: Claus Holm Larsen         ############
##############################################################


import doctest  # Do not change or remove this line.


def common_items(list_a, list_b):
    """(list, list) --> list

    Iteratively compares the content of list_a with list_b and
    returns a list of common elements.

    >>> common_items([1, 2, 4, 6], [3, 4, 7, 9])
    [4]
    >>> common_items(['Peter', 'Linda', 'John'], ['Louis', 'Margareth', 'Peter', 'Joni', 'Linda'])
    ['Peter', 'Linda']
    >>> common_items([1, 2, 4, 6], [3, 7, 9, 15])
    []
    >>> common_items([1, 2, 4, 6], [])
    []
    >>> common_items([], [3, 7, 9, 15])
    []
    >>> common_items([], [])
    []
    """

    common = []
    seta=set(list_a)
    setb=set(list_b)
    setc=seta.intersection(setb)
    common=list(setc)
    # Write your code here.

    return common   # Do not change or remove this line.

print doctest.testmod(verbose=True)     # Do not change or remove this line.

