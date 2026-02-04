def p_add(expr): 
    return expr[0] + expr[2]

def p_subtract(expr): 
    return expr[0] - expr[2]

def p_multiply(expr): 
    return expr[0] * expr[2]

def p_idivide(expr): 
    return expr[0] // expr[2]

def p_fdivide(expr): 
    return expr[0] / expr[2]

def p_exp(expr): 
    return expr[0] ** expr[2]
