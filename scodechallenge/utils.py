from typing import List


def getItemsList(items_list:List) ->List:
    """A simple function for formatting lists"""
    new_item = []
    for item in items_list:
        if type(item) != list:
            new_item.append(item)
        else:
            new_item+=getItemsList(item)
    return new_item
