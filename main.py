from core.input import get_mode, get_input


def main():
    mode = get_mode()
    value = get_input()
    print(mode)
    print(value)


if __name__ == "__main__":
    main()
