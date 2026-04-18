import sys
from contracts import make_failure
from errors import INTERNAL_ERROR


from core.input import get_mode, get_input, build_request
from core.handle import validate_reqest
from core.normalize import normalize_request
from encode.bits_encoder import build_bit_stream
from encode.groups import _6bit_groups
from encode.base64 import get_base64

from decode.validate import validate
from decode.index import get_index_list
from decode._6bit_groups import get_6bit_groups
from decode._8bit_groups import get_8bit_groups
from decode.bytes import get_byte_list
from decode.text import get_final_text


def main():
    mode = get_mode()
    value = get_input()
    request = build_request(mode, value)
    validated_request = validate_reqest(request)
    normalized_request = normalize_request(validated_request)

    mode = normalized_request.get("mode")

    if mode == "encode":
        bit_stream = build_bit_stream(normalized_request)
        output = _6bit_groups(bit_stream)
        final_result = get_base64(output, normalized_request["byte_length"])

        if not final_result["ok"]:
            output = make_failure(INTERNAL_ERROR, "Error getting final base64 - (main)")
            print(output)
            sys.exit()

        print(
            f"Ok: {final_result.get("ok")}\nMode: {final_result.get("mode")} | Result Text: {final_result.get("base64_text")}\nError: {final_result.get("error")}"
        )

    else:
        is_ok = validate(normalized_request["base64_text"])

        if not is_ok:
            output = make_failure(
                INTERNAL_ERROR, "Error Invalid Base64 - (main) [ERROR - 1] "
            )
            print(output)
            sys.exit()
        data = get_index_list(normalized_request["base64_text"])
        _6bit_groups_decode = get_6bit_groups(data["index_list"])
        _8bit_groups = get_8bit_groups(_6bit_groups_decode, data["padding_length"])
        byte_list = get_byte_list(_8bit_groups)
        final_result_decode = get_final_text(byte_list)

        if not final_result_decode["ok"]:
            output = make_failure(INTERNAL_ERROR, "Error getting final text - (main)")
            print(output)
            sys.exit()

        print(
            f"Ok: {final_result_decode.get("ok")}\nMode: {final_result_decode.get("mode")} | Result Text: {final_result_decode.get("text")}\nError: {final_result_decode.get("error")}"
        )


if __name__ == "__main__":
    main()
