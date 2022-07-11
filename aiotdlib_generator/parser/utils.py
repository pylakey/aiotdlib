import re


def upper_first(s: str) -> str:
    return s[:1].upper() + s[1:]


def lower_first(s: str) -> str:
    return s[:1].lower() + s[1:]


def snake_case(s: str) -> str:
    """
    Convert camel case string to snake case.

    :param s: Some camel case string
    :return: Snake case string
    """
    if not s:
        return ""

    s = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s).lower()
