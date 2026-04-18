import sys


def get_8bit_groups(_6bit_groups, padding_length):

    bit_stream = "".join(_6bit_groups)

    remove_bits = padding_length * 2

    bit_stream = bit_stream[:-remove_bits]

    _8bit_groups = []

    for i in range(0, len(bit_stream), 8):
        group = bit_stream[i : i + 8]
        _8bit_groups.append(group)

    return _8bit_groups
