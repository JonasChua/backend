# tests/common/utility.py


def parse_error(error: dict[str, str]) -> tuple[str, str]:
    assert "detail" in error, error
    detail = error["detail"]
    assert "::" in detail, detail
    error_code, _, message = detail.partition("::")
    return error_code, message
