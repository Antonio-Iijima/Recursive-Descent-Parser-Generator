def p_mathexpr(expr):
    return expr[0]

def p_add(expr): 
    print(expr)
    return expr[0] + expr[1]

def p_subtract(expr): 
    return expr[0] - expr[1]

def p_term(expr): 
    return expr[0]

def p_multiply(expr): 
    return expr[0] * expr[1]

def p_divide(expr):
    return expr[0]

def p_factor(expr): 
    match len(expr):
        case 3: return expr[1]
        case 2: return -expr[1]
        case _: return expr[0]

def p_abs(expr):
    return abs(expr[0])

def p_idivide(expr): 
    return expr[0] // expr[1]

def p_fdivide(expr): 
    return expr[0] / expr[1]

def p_exp(expr): 
    return expr[0] ** expr[1]