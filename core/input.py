from contracts import make_failure
from errors import INVALID_MODE
from errors import MODE_MISSING
from errors import INVALID_INPUT_KIND
from constants import VALID_MODES
import sys


def get_mode():
    mode = input("Enter Mode (encode/decode):").strip()
    if not mode:
        output = make_failure(MODE_MISSING, "Mode input is empty - (get_mode)")
        print(output["error"])
        sys.exit()

    if mode not in VALID_MODES:
        output = make_failure(
            INVALID_MODE, "valid modes are (encode/decode) - (get_mode)"
        )
        print(output["error"])
        sys.exit()

    return mode


def get_input():
    value = input("Enter the Value:").strip()
    if not value or value == None:
        output = make_failure(
            INVALID_INPUT_KIND, "Input is empty please enter something - (get_input)"
        )
        print(output["error"])
        sys.exit()

    return value


def build_request(mode, value):

    input_kind = "text" if mode == "encode" else "base64"
    request = {"mode": mode, "raw_input": value, "input_kind": input_kind}

    return request
