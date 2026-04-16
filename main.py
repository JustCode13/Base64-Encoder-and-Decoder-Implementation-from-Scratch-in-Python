from core.input import get_mode, get_input, build_request
from core.handle import validate_reqest
from core.normalize import normalize_request
from encode.bits_encoder import build_bit_stream


def main():
    mode = get_mode()
    value = get_input()
    request = build_request(mode, value)
    validated_request = validate_reqest(request)
    normalized_request = normalize_request(validated_request)

    mode = normalized_request.get("mode")

    if mode == "encode":
        build_bit_stream(normalized_request)


if __name__ == "__main__":
    main()
