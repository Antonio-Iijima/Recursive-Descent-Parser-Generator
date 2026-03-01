g_env = {}
g_markers = {}



#! <statement> ::= <assignment> NEWLINE | <conditional> NEWLINE | <return> NEWLINE | <goto> NEWLINE | <print> NEWLINE 
def p_statement(expr):
    expr(0)    


def p_statement_list_0(expr):
    expr(0)
    
#! <statement_list> ::= <statement> | <statement> NEWLINE <statement_list> 
def p_statement_list_1(expr):
    expr(0)
    expr(1)


def p_assignment(expr):
    g_env[expr(1)] = expr(3)


def p_string(expr):
    return expr(1)


#! <if_then> ::= if <comparison>, then NEWLINE <block>
def p_if_then(expr):
    if expr(1): 
        expr(4)

#! <if_then_else> ::= if <comparison>, then NEWLINE <block> else NEWLINE <block>
def p_if_then_else(expr):
    if expr(1):
        expr(4)
    else: 
        expr(6)

#! <block> ::= INDENT <statement_list> DEDENT
def p_block(expr):
    return expr(1)


def p_return(expr):
    raise Exception(0, expr(1))


def p_marker(expr):
    g_markers[expr(1)] = lambda: expr(2)
    expr(2)

def p_jump(expr):
    g_markers[expr(2)]()


def p_label(expr):
    try:
        return g_env[expr(0)]
    except KeyError:
        raise Exception(1, f"Error: variable {expr(0)} not declared.")


def p_print(expr):
    print(expr(1))
