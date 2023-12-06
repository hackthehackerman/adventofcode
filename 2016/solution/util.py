import hashlib


def toLines(fileName: str) -> list:
    with open(fileName, "r") as f:
        return f.readlines()


def toString(fileName: str) -> str:
    with open(fileName, "r") as f:
        return f.read()


def md5_str(s):
    return hashlib.md5(s.encode("utf-8")).hexdigest()
