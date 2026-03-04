def p_op_index(expr):
    return expr(0)[expr(2)]

def p_op_head(expr):
    return expr(1)[0]

def p_op_tail(expr):
    return expr(1)[1:]

def p_op_cons(expr):
    return [expr(1)] + expr(2)
