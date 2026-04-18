import sys
from constants import BASE64_ALPHABET
from contracts import make_failure
from errors import INTERNAL_ERROR


def validate(base64):
    for ch in base64:
        if ch not in BASE64_ALPHABET and ch != "=":
            output = make_failure(
                INTERNAL_ERROR, "Error Invalid Base64 - (validate) [ERROR - 1] "
            )
            print(output)
            sys.exit()

    padding_index = base64.find(ch)

    if padding_index != -1 and any(ch != "=" for ch in base64[padding_index:]):
        output = make_failure(
            INTERNAL_ERROR, "Error Invalid Base64 - (validate) [ERROR - 2] "
        )
        print(output)
        sys.exit()

    padding_length = len(base64[padding_index:])

    if padding_length not in (0, 1, 2):
        output = make_failure(
            INTERNAL_ERROR, "Error Invalid Base64 - (validate) [ERROR - 3] "
        )
        print(output)
        sys.exit()

    if base64 and len(base64) % 4 != 0:
        output = make_failure(
            INTERNAL_ERROR, "Error Invalid Base64 - (validate) [ERROR - 4] "
        )
        print(output)
        sys.exit()

    return True
