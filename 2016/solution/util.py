def toLines(fileName: str) -> list:
    with open(fileName, "r") as f:
        return f.readlines()


def toString(fileName: str) -> str:
    with open(fileName, "r") as f:
        return f.read()
