from core.input import get_mode, get_input, build_request
from core.handle import validate_reqest
from core.normalize import normalize_request


def main():
    mode = get_mode()
    value = get_input()
    request = build_request(mode, value)
    validated_request = validate_reqest(request)
    normalized_request = normalize_request(validated_request)

    print(normalized_request)


if __name__ == "__main__":
    main()
