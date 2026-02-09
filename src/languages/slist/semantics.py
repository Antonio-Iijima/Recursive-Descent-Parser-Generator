def p_symbolexpr(expr): 
    return expr[0] if len(expr) == 1 else f"({expr[1]})"

def p_slist(expr):
    return "".join({None: " "}.get(c, c) for c in expr)
