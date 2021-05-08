'''
 
    line -> nline line | nline
    nline -> dtype var SCOLON | STR var SCOLON
    nline ->  fline
    fline : dtype numexp | numexp  
    numexp -> assign SCOLON
    exp -> exp PLUS term | exp MINUS term | term
    term -> term MUL fact | term DIV fact | term MOD fact | fact
    fact -> INTEGER | FLOAT | varval | bval | CHAR
    bval -> TRUE | FALSE
    varval -> var | var LBB exp RBB
    var : IDVAR
    dtype -> INT | FLT | CHR | BOOL
    nline -> STR IDVAR EQUAL strvar SCOLON
    strvar -> STRING | varval

    nline : BOOL MAIN LPAREN RPAREN lcb line rcb 
    nline : RETURN LPAREN bval RPAREN SCOLON
    nline : EXIT LPAREN RPAREN SCOLON
    nline : PRINT LPAREN pline RPAREN SCOLON
    pline : exp | STRING

    nline : ifsts
    ifsts : IF LPAREN bexp RPAREN lcb line rcb elsests
    elsests : ELSE lcb line rcb | ELSE ifsts | empty

    lcb : LCB
    rcb : RCB

    bexp : bexp andor bexp2 | bexp2
    bexp2 : bexp2 rln exp | exp
    rln : DEQUAL | GTHEN | LTHEN | NOT
    andor : AND | OR
    
    empty :

    nline : FOR LPAREN fline bexp SCOLON assign RPAREN lcb line rcb
    nline : WHILE LPAREN bexp RPAREN lcb line rcb
    assign : assvar EQUAL exp | assvar EQUAL STRING
 

    nline : dtype LBB RBB IDVAR EQUAL arrt SCOLON | STR LBB RBB IDVAR EQUAL arrt SCOLON 
    arrt : var | LCB dws RCB
    dws : factarr COM dws | factarr
    factarr : fact | STRING
'''

import ply.yacc as yacc
from claclex import tokens
from symb_tbl import *

def p_line_chg(p):
    '''line : nline line 
            | nline'''

def p_nline_init(p):
    '''nline : dtype var SCOLON
                | STR var SCOLON'''
    store(p[2],p[1])
    
def p_nline_dec(p):
    'nline : fline'
    p[0] = p[1]

    print()
    for st in stk:
        print(st)
    print()

def p_nline_str(p):
    'nline : STR IDVAR EQUAL strvar SCOLON'
    store(p[2],p[1],p[4]['value'],p[4]['line'])
    
def p_nline_main(p):
    'nline : BOOL MAIN LPAREN RPAREN lcb line rcb'

def p_nline_ret(p):
    'nline : RETURN LPAREN bval RPAREN SCOLON'

def p_nline_if(p):
    'nline : ifsts'

def p_nline_exit(p):
    'nline : EXIT LPAREN RPAREN SCOLON'

def p_nline_print(p):
    'nline : PRINT LPAREN pline RPAREN SCOLON'

def p_pline_print(p):
    '''pline : exp
            | STRING'''
    print(p[1])

def p_nline_for(p):
    'nline : FOR LPAREN fline bexp SCOLON assign RPAREN lcb line rcb'

def p_nline_while(p):
    'nline : WHILE LPAREN bexp RPAREN lcb line rcb'

def p_ifsts_fst(p):
    'ifsts : IF LPAREN bexp RPAREN lcb line rcb elsests'
    
def p_rcb_scppop(p):
    'rcb : RCB'
    remove_scope()

def p_lcb_scppush(p):
    'lcb : LCB'
    add_scope()

def p_elsests_fst(p):
    '''elsests : ELSE lcb line rcb 
                | ELSE ifsts
                | empty'''

def p_numexp_stm(p):
    'numexp : assign SCOLON'
    p[0] = p[1]

def p_exp_pm(p):
    '''exp : exp PLUS term 
           | exp MINUS term 
           | term'''
    if(len(p)==4):
        print(p[1],p[3])
        if(not p[1]['type'] == p[3]['type']):
            print('ERROR: Type mismatched in line:',p[1]['line'])
            exit()
        p1 = p[1]['value']
        p3 = p[3]['value']
        p0 = None
        # if(p[2] == '+'):
        #     p0 = p1 + p3
        #     pass
        # else:
        #     p0 = p1 - p3

        p[0] = {'value':p0, 'type': p[1]['type'], 'line':p[1]['line']}
    else:
        p[0] = p[1]

def p_term_mdm(p):
    '''term : term MUL fact
            | term DIV fact
            | term MOD fact
            | fact'''

    if(len(p)==4):
        if(not p[1]['type'] == p[3]['type']):
            print('ERROR: Type mismatched in line:',p[1]['line'])
            exit()
        p1 = p[1]['value']
        p3 = p[3]['value']
        p0 = None
        if(p[2] == '*'):
            p0 = p1 * p3
        elif(p[2] == '/'):
            p0 = p1 / p3
        else:
            p0 = p1 % p3  

        p[0] = {'value':p0, 'type': p[1]['type'], 'line':p[1]['line']}
          
    else:
        p[0] = p[1]


def p_fact_val(p):
    '''fact : INTEGER 
            | FLOAT 
            | varval
            | bval
            | CHAR'''
    p[0] = p[1]

def p_varval_val(p):
    '''varval : var
              | var LBB exp RBB'''
    
    p0 = lookup(p[1])
    if(len(p) == 5):
        if(p0['type'] != 'array'):
            print('TYPE ERROR! {} is not an array'.format(p[1]))
            exit()
        if(p[3]['type'] != 'int'):
            print('TYPE ERROR! array index cannot be of {} type'.format(p[3]['type']))
            exit()
        #TODO: cal val of array using index and address
        p[0] = {'type': p0['arraytype'],'line':p0['line'], 'value':p0['value']}
    else:
        p[0] = p0

def p_assvar_val(p):
    '''assvar : var
              | var LBB exp RBB'''
    
    p0 = lookup_init(p[1])
    if(not p0):# a
        p[0] = p[1]
        return
    if(len(p) == 5):#a[12]
        if(p0['type'] != 'array'):
            print('TYPE ERROR! {} is not an array'.format(p[1]))
            exit()
        if(p[3]['type'] != 'int'):
            print('TYPE ERROR! array index cannot be of {} type'.format(p[3]['type']))
            exit()
        #TODO: cal val of array using index and address
        p[0] = {'type': p0['type'],'line':p0['line'], 'arraytype': p0['arraytype'] ,'value':p0['value'], 'name': p[1]}
    else:
        p0['name'] = p[1]
        p[0] = p0

def p_bval_val(p):
    '''bval : TRUE
            | FALSE'''
    p[0] = p[1]

def p_var_id(p):
    '''var : IDVAR'''
    p[0] = p[1]


def p_dtype_num(p):
    '''dtype : INT 
            | FLT 
            | CHR 
            | BOOL'''
    p[0] = p[1]

def p_strvar_val(p):
    '''strvar : STRING 
            | varval'''
    if(p[1]['type'] == 'string'):
        p[0] = p[1]
    else:
        print("TYPE ERROR {} is not same as string".format(p[1]['type']))
        exit()

def p_bexp_fst(p):
    '''bexp : bexp andor bexp2 
            | bexp2'''
    if(len(p) == 4):
        pass
    else:
        p[0] = p[1]

def p_bexp2_fst(p):
    '''bexp2 : bexp2 rln exp 
            | exp'''
    if(len(p)==4):
        pass
    else:
        p[0] = p[1]

def p_rln_fst(p):
    '''rln : DEQUAL 
            | GTHEN 
            | LTHEN 
            | NOT'''
    p[0] = p[1]

def p_andor_fst(p):
    '''andor : AND 
            | OR'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_assign_num(p):
    '''assign : assvar EQUAL exp
              | assvar EQUAL STRING'''
    if(not p[3]):
        print('ERROR! variable used before assigned!!')
        exit()
    tval = p[3].copy()
    if(type(p[1]) == str):
        tval['name'] = p[1]
        p[0] = tval
    else:
        ttype = p[1]['type']
        if(ttype == 'array'):
            ttype = p[1]['arraytype']
        if(tval['type'] != ttype):
            print("TYPE ERROR! {} doesn't match with {} in lineno: {}".format(tval['type'],p[1]['type'],tval['line']))
            exit()
        p[1]['value'] = tval['value']
        p[1]['line'] = tval['line']
        p[0] = p[1]

def p_fline_for(p):
    '''fline : dtype numexp 
            | numexp'''

    if(len(p) == 3):
        if( p[2]['type'] != p[1]):
            print("ERROR: Missmached type at line:",p[2]['line'])
            exit()
        store(p[2]['name'],p[1],p[2]['value'],p[2]['line'])
    else:
        tval = lookup(p[1]['name'])
        if( p[1]['type'] != tval['type']):
            print("ERROR: Missmached type: {} not matched with {} datatype".format(p[1]['name'],p[1]['type']))
            exit()
        # st[p[1]['name']]['value'] = p[1]['value']
        update_spe(p[1]['name'],['value'],[p[1]['value']])

def p_nline_arr(p):
    '''nline : dtype LBB RBB IDVAR EQUAL arrt SCOLON
                | STR LBB RBB IDVAR EQUAL arrt SCOLON'''

    #TODO: ADD a way to give size in array at initialization
    if(p[6]['type']== 'array'):
        if(p[1] != p[6]['arraytype']):
            print("Array Type error in {}!".format(p[4]))
            exit()
    else:
        if(p[1] != p[6]['type']):
            print("Type error in {}!".format(p[4]))
            exit()
    store(p[4],'array', arraytype= p[1])
            

def p_arrt_data(p):
    '''arrt : var 
            | LCB dws RCB'''
    if(len(p) == 4):
        p[0] = p[2]
    else:
        temp = lookup(p[1])
        if(temp['type'] != 'array'):
            print("ERROR! {} is not an array".format(p[1]))
            exit()
        p[0] = temp

def p_dws_vals(p):
    '''dws : factarr COM dws 
            | factarr'''
    if(len(p) == 4):
        if(p[1]['type'] != p[3]['type']):
            print('TYPE ERROR!!')
            exit()
        p[0] = p[1]
    else:
       p[0] = p[1] 

def p_factarr_vals(p):
    '''factarr : fact 
    | STRING'''
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    print(p)
    exit()

# Build the parser
parser = yacc.yacc()

f = open('demo.tam')
data = f.read()

result = parser.parse(data)
print(result)




'''
print(45 + 56 * 3 /50 +23 %5+ 21 + 51);
float a;
int b = 45;
int c = 45 + 56 * 3 /50 +23 %5+ 21 + 51;
string abc;
float d = 45.1 + 56.0;
a = d;
string abcd = "ayush";
abc = "agarwal";
b = c;
int jav = 45;
int kav = 50;
int res = 45+50;
res = res+jav;
res = res+kav;
float f1 = 45.2;
string trrs;
boolean b1 = true;
string s1 = "Ayush Agarwal";
string s2 = s1;
string a1 = "ajsb";
char ch = '5';
#string res;

'''


"TODO: correct assign"