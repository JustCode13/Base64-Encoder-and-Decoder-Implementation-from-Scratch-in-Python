from contracts import make_failure
from errors import INTERNAL_ERROR
import sys


def _6bit_groups(bit_stream):

    if not bit_stream:
        output = make_failure(INTERNAL_ERROR, "Bit Stream Empty - (_6bit_groups)")
        print(output)
        sys.exit()

    groups = []
    for i in range(0, len(bit_stream), 6):
        groups.append(bit_stream[i : i + 6])

    last = groups[-1]

    if len(last) < 6:

        missing = 6 - len(last)

        padded = last.ljust(6, "0")

        groups[-1] = padded

        return {
            "ok": True,
            "bit_stream_length": len(bit_stream),
            "missing_bits": missing,
            "six_bit_groups": groups,
        }

    else:
        return {
            "ok": True,
            "bit_stream_length": len(bit_stream),
            "missing_bits": 0,
            "six_bit_groups": groups,
        }
