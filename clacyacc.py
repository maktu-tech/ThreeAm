import ply.yacc as yacc

from claclex import tokens


vars = {}
pyth = False


def p_lan_chg(p):
    '''lan : pyt
            | line'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_pyt_chg(p):
    'pyt : PYT lineP'

def p_lineP_rep(p):
    '''lineP : nlineP lineP
            | nlineP'''
    p[0] = p[1]

def p_nlineP_var(p):
    'nlineP : var EQUAL expression'
    vars[p[1]] = p[3]
    print(vars)

def p_nlineP_exit(p):
    'nlineP : EXIT LPAREN RPAREN'
    exit()

def p_nlineP_print(p):
    'nlineP : PRINT LPAREN var RPAREN'
    print(vars[p[3]])

def p_line_rep(p):
    '''line : nline line
            | nline
            | pyt'''
    p[0] = p[1]


def p_nline_var(p):
    '''nline : INTEGER var EQUAL expression SEMICOLON'''
    if not p[2] in vars:
        vars[p[2]] = p[4]
        print(vars)

def p_nline_var_update(p):
    'nline : var EQUAL expression SEMICOLON'
    if p[1] in vars:
        vars[p[1]] = p[3]
        p[0] = p[3]

def p_nline_exit(p):
    'nline : EXIT LPAREN RPAREN SEMICOLON'
    exit()

def p_nline_print(p):
    'nline : PRINT LPAREN var RPAREN SEMICOLON'
    print(vars[p[3]])

def p_var_id(p):
    'var : IDVAR'
    p[0] = p[1]

# def p_expression_var(p):
#     'expression : var'
#     p[0] = vars[p[1]]

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    '''factor : NUMBER
              | var'''
    if p[1] in vars:
        p[0] = vars[p[1]]
    elif type(p[1]) == type(0):
        p[0] = p[1]
    else:
        print('error')

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

# while True:
#    try:
#        s = input('calc > ')
#    except EOFError:
#        break
#    if not s: continue
#    result = parser.parse(s)
#    print(result)

data = ''' 
int jav = 45;
int kav = 50;
int res = 45+50;
res = res+jav;
res = res+kav;

#python
pyt = 100
res = pyt+res
exit()
'''

result = parser.parse(data)
print(result)