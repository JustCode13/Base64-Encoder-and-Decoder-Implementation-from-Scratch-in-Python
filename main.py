from core.input import get_mode, get_input, build_request
from core.handle import validate_reqest
from core.normalize import normalize_request
from encode.bits_encoder import build_bit_stream
from encode.groups import _6bit_groups
from encode.base64 import get_base64


from decode.index import get_index_list
from decode._6bit_groups import get_6bit_groups
from decode._8bit_groups import get_8bit_groups


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

        print(
            f"Ok: {final_result.get("ok")}\nMode: {final_result.get("mode")} | Result Text: {final_result.get("base64_text")}\nError: {final_result.get("error")}"
        )

    else:
        data = get_index_list(normalized_request["base64_text"])
        _6bit_groups = get_6bit_groups(data["index_list"])
        _8bit_groups = get_8bit_groups(_6bit_groups, data["padding_length"])

        print(_8bit_groups)


if __name__ == "__main__":
    main()
