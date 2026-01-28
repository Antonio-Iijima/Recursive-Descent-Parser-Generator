import re



re_terminal: str = r"<[A-Z][a-zA-Z]*>"


def is_nonterminal(prod: str) -> bool: return not (re.fullmatch(re_terminal, prod) == None)


def is_terminal(prod: str) -> bool: return not is_nonterminal(prod)


def embed_nonterminal(s: str) -> str: return s[1:-1] if is_nonterminal(s) else s


def split_nonterminals(prod: str) -> list:
    out = []
    nextWord = False

    for c in prod:
        if nextWord:
            out.append("")
            nextWord = False

        match c:
            case "<":
                out.append(c)
            case ">":
                out[-1] += c
                nextWord = True
            case _:
                if not out: out.append(c)
                else: out[-1] += c

    return out


def compare(a: list, b: list) -> bool:
    """Check if all the elements of `a` and `b` match. Assumes lists are of the same length."""

    def comparative(x): return x if isinstance(x, str) else x.name
    a, b = [x for x in a if not x == "ε"], [y for y in b if not y == "ε"]

    for x, y in zip(a, b):
        if not comparative(x) == comparative(y): return False
    return True
