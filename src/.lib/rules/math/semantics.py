def p_number(expr): 
    return expr[0] if len(expr) == 1 else -expr[-1]

def p_float(expr): 
    return float("".join(map(str, expr)))

def p_int(expr): 
    return int("".join(map(str, expr))) if len(expr) == 2 else int(expr[0])

def p_digit(expr): 
    return int(expr[0])
