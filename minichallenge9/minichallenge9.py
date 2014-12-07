# # Beginners mini challenge no. 9. Python version 2.7.

##############################################################
######### Published to Python Programming Society ############
#########              October 2014               ############
#########       Author: Claus Holm Larsen         ############
##############################################################

import doctest      # Do not change or remove this line.

def compress_list(my_list):
    """ (list of str) -> list of str

    Return a new list with adjacent pairs of string elements from L
    concatenated together, starting with indices 0 and 1, 2 and 3,
    and so on.

    Precondition: len(my_list) >= 2 and len(my_list) % 2 == 0

    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']
    >>> compress_list(['a', 'b', 'c', 'd','e', 'f', 'g', 'h'])
    ['ab', 'cd', 'ef', 'gh']
    >>> compress_list(['Peter', 23, 'Andrew', 19, 'Susan', 18, 'Lily', 22])
    ['Peter23', 'Andrew19', 'Susan18', 'Lily22']
    >>> compress_list([22, 'Lily', 18, 'Susan', 19, 'Andrew', 23, 'Peter'])
    ['22Lily', '18Susan', '19Andrew', '23Peter']
    """

    compressed_list = []       # Do not change or remove this line.
    # Write your code here.        
    compressed_list=[str(my_list[i])+str(my_list[i+1]) for i in range(0,len(my_list),2)]
    return compressed_list      # Do not change or remove this line.


print doctest.testmod(verbose=True)        # Do not change or remove this line.

