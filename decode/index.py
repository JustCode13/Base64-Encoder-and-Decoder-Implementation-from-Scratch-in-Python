from constants import BASE64_ALPHABET


def get_index_list(base46):

    base64_chars = base46.rstrip("=")

    padding_length = len(base46) - len(base64_chars)

    index_list = []

    for ch in base64_chars:
        index = BASE64_ALPHABET.find(ch)
        index_list.append(index)

    return {"ok": True, "index_list": index_list, "padding_length": padding_length}
