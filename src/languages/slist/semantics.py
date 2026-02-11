def p_symbolexpr(v, expr): 
    match v:
        case 3: return f"({expr[0]})"
        case _: return expr[0]
    
def p_slist(v, expr):
    return "".join(expr)
