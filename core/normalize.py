from errors import INTERNAL_ERROR
from contracts import make_failure
import sys


def normalize_encode_request(value):
    try:
        mode = value.get("mode")
        raw_input = value.get("raw_input")

        raw_input_len = len(raw_input)
        encoded_raw_input = raw_input.encode("utf-8")

    except:
        output = make_failure(INTERNAL_ERROR, "Error on - (normalize_encode_input)")
        print(output["error"])
        sys.exit()

    return {
        "ok": True,
        "mode": mode,
        "data_bytes": encoded_raw_input,
        "byte_length": raw_input_len,
    }


def normalize_decode_request(value):
    try:
        mode = value.get("mode")
        base64_text = value.get("raw_input")

        base64_text_len = len(base64_text)
        mode = value.get("mode")
        base64_text = value.get("raw_input")

        base64_text_len = len(base64_text)
    except:
        output = make_failure(INTERNAL_ERROR, "Error on - (normalize_decode_input)")
        print(output["error"])
        sys.exit()

    return {
        "ok": True,
        "mode": mode,
        "base64_text": base64_text,
        "base64_len": base64_text_len,
    }


def normalize_request(request):
    try:
        value = request.get("value")
        mode = value.get("mode")

        data = {}

        if mode == "encode":
            data = normalize_encode_request(value)

        elif mode == "decode":
            data = normalize_decode_request(value)

        return data
    except:
        output = make_failure(INTERNAL_ERROR, "Error on - (normalize_request)")
        print(output["error"])
        sys.exit()
