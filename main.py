from core.input import get_mode, get_input, build_request
from core.handle import validate_reqest


def main():
    mode = get_mode()
    value = get_input()
    request = build_request(mode, value)
    data = validate_reqest(request)
    print(data)


if __name__ == "__main__":
    main()
