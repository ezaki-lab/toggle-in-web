import hashlib
from random import randint


def generate_token() -> str:
    return (
        hashlib.sha3_256(
            str(randint(0, 999999)).encode("utf-8")
        ).hexdigest()
    )
