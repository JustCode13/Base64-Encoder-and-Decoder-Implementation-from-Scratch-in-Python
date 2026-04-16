from contracts import make_failure
from errors import INVALID_REQUEST
from errors import INTERNAL_ERROR
import sys


def validate_reqest(request):

    if not isinstance(request, dict):
        output = make_failure(
            INVALID_REQUEST, "The request doesn't have proper data type"
        )
        print(output["error"])
        sys.exit()

    mode = request.get("mode")
    raw_input = request.get("raw_input")
    input_kind = request.get("input_kind")

    if not mode or not raw_input or not input_kind:
        output = make_failure(
            INTERNAL_ERROR, "The request doesn't contain any data - (validate_request)"
        )
        print(output["error"])
        sys.exit()

    if input_kind not in ("text", "base64"):
        output = make_failure(
            INTERNAL_ERROR,
            "Input kind doesn't container required input - (validate_request)",
        )
        print(output["error"])
        sys.exit()

    if mode == "encode" and not input_kind == "text":
        output = make_failure(
            INTERNAL_ERROR,
            "Invalid input kind - (validate_request)",
        )
        print(output["error"])
        sys.exit()

    return {"ok": True, "value": request, "error": None}
