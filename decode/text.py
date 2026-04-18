import sys
from contracts import make_failure
from errors import INTERNAL_ERROR


def get_final_text(byte_list):

    byte_obj = bytes(byte_list)

    try:
        text = byte_obj.decode("utf-8")
    except UnicodeDecodeError:
        output = make_failure(
            INTERNAL_ERROR, "Error getting final text - (get_final_text)"
        )
        print(output)
        sys.exit()

    return {"ok": True, "mode": "decode", "text": text, "error": None}
