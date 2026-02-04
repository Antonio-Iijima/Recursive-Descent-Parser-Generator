def p_expr(expr):
    return expr[0]

def p_term(expr): 
    return expr[0]

def p_divide(expr):
    return expr[0]

def p_factor(expr): 
    return expr[1] if len(expr) == 3 else expr[0]
