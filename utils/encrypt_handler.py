import hashlib
from utils.secrets import PASSWORD

def encryption_check(password: str):
    password = hashlib.sha512(bytes(password, "utf-8")).hexdigest()

    if password == PASSWORD:
        return True
    else:
        return False