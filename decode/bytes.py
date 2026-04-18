import sys


def get_byte_list(_8bit_groups):
    byte_list = []

    for group in _8bit_groups:

        byte = int(group,2)
        byte_list.append(byte)

    return byte_list