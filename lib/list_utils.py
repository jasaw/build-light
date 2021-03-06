"""list utils"""

from copy import deepcopy

def flatten_list(nested_list):
    """
    Flatten an arbitrarily nested list, without recursion (to avoid stack
    overflows). Returns a new list, the original list is unchanged.
    >> list(flatten_list([1, 2, 3, [4], [], [[[[[[[[[5]]]]]]]]]]))
    [1, 2, 3, 4, 5]
    >> list(flatten_list([[1, 2], 3]))
    [1, 2, 3]
    """
    nested_list = deepcopy(nested_list)
    while nested_list:
        sublist = nested_list.pop(0)
        if isinstance(sublist, list):
            nested_list = sublist + nested_list
        else:
            yield sublist

def list_items_unique(list_to_verify):
    """
    Verifies that all items are unique.
    Returns True if unique, otherwise False.
    """
    tmp_list = list(flatten_list(list_to_verify))
    if len(tmp_list) > len(set(tmp_list)):
        return False
    return True

def find_list_given_value(nested_list, value):
    """
    Returns the list that contains the specified value.
    >> tuple(find_list_given_value([['abc', '123'], 'def', ['000', ['123', '456'], '999']], '123'))
    (['abc', '123'], ['123', '456'])
    >> tuple(find_list_given_value([['abc', '123'], 'def', ['000', ['123', '456'], '999']], '010'))
    ()
    """
    for item in nested_list:
        if isinstance(item, list):
            for found in find_list_given_value(item, value):
                yield found
        if item == value:
            yield nested_list

def remove_first_item(nested_list):
    """
    Removes the first element of the deepest list.
    >>> tuple(remove_first_item([['abc','def','ghi'],['123','456','789'],[['000','999'],['AAA','BBB']]]))
    (['def', 'ghi'], ['456', '789'], [['999'], ['BBB']])
    """
    for item in nested_list:
        if isinstance(item, list):
            yield list(remove_first_item(item))
        elif nested_list.index(item) != 0:
            yield item
