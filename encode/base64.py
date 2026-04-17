from constants import BASE64_ALPHABET


def get_base64(output, byte_length):
    groups = output["six_bit_groups"]

    base64_alphabet_list = []
    for group in groups:
        index = int(group, 2)
        base64_alphabet = BASE64_ALPHABET[index]
        base64_alphabet_list.append(base64_alphabet)

    base64_unpadded_text = "".join(base64_alphabet_list)

    remainder = byte_length % 3

    padding = None

    if remainder == 0:
        padding = ""
    elif remainder == 1:
        padding = "=="
    elif remainder == 2:
        padding = "="

    padded_base64 = base64_unpadded_text + padding

    return {"ok": True, "mode": "encode", "base64_text": padded_base64, "error": None}
