def make_success(value):
    output = {"ok": True, "value": value, "error": None}
    return output


def make_failure(error_type, message):
    output = {
        "ok": True,
        "value": None,
        "error": {"error_type": error_type, "message": message},
    }
    return output
