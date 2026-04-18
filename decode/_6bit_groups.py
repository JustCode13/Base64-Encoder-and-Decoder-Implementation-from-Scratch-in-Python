import sys


def get_6bit_groups(index_list):

    _6bit_groups = []

    for index in index_list:
        group = format(index, "06b")
        _6bit_groups.append(group)

    return _6bit_groups
