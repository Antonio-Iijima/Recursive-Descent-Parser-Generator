def p_program(expr): 
    return expr[0] if len(expr) == 1 else expr[1:-1]

def p_atom(expr):
    return expr[0]

def p_symbol(expr):
    return expr[0]

def p_id(expr):
    return expr[0]

def p_list(expr):
    return expr

def p_atoms(expr):
    return expr
