def p_symbolexpr(expr): 
    return expr[0] if len(expr) == 1 else f"({expr[1]})"

def p_slist(expr):
    return f"{expr[0]}, {expr[2]}" if len(expr) == 3 else expr[0]
