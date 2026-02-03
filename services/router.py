from enum import Enum


class Intent(str, Enum):
    DOCUMENT = "document"
    DATABASE = "database"
    GENERAL = "general"


def route_intent(query: str) -> Intent:
    q = query.lower()

    if any(k in q for k in [
        "policy", "document", "pdf", "leave", "entitled"
    ]):
        return Intent.DOCUMENT

    if any(k in q for k in [
        "count", "total", "sum", "average", "how many records"
    ]):
        return Intent.DATABASE

    return Intent.GENERAL
