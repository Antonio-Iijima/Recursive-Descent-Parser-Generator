import re



re_terminal: str = r"<[A-Z][a-zA-Z]*>"


def is_nonterminal(prod: str) -> bool:
    return not (re.fullmatch(re_terminal, prod) == None)


def is_terminal(prod: str) -> bool: return not is_nonterminal(prod)


def embed_nonterminal(s: str) -> str: return s[1:-1] if is_nonterminal(s) else s


def tokenize(prod: str) -> list:
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
