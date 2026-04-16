def byte_to_8bit_string(byte):

    bits = format(byte, "08b")
    return bits


def build_bit_stream(request):
    bytes = request.get("data_bytes")
    bits = []

    for byte in bytes:
        _8bits = byte_to_8bit_string(byte)
        bits.append(_8bits)

    bit_stream = "".join(bits)

    print(bit_stream)
