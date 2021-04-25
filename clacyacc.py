'''
    line -> nline line | nline
    nline -> dtype var SCOLON | STR var SCOLON
    nline ->  fline
    fline : dtype numexp | numexp
    numexp -> assign SCOLON
    exp -> exp PLUS term | exp MINUS term | term
    term -> term MUL fact | term DIV fact | term MOD fact | fact
    fact -> INTEGER | FLOAT | var | bval | CHAR
    bval -> TRUE | FALSE
    var -> IDVAR | IDVAR LBB INTEGER RBB | IDVAR LBB IDVAR RBB
    dtype -> INT | FLT | CHR | BOOL
    nline -> STR IDVAR EQUAL strvar SCOLON
    strvar -> STRING | var

    nline : BOOL MAIN LPAREN RPAREN LCB line RCB
    nline : RETURN LPAREN bval RPAREN SCOLON
    nline : EXIT LPAREN RPAREN SCOLON
    nline : PRINT LPAREN pline RPAREN SCOLON
    pline : exp | STRING

    nline : ifsts
    ifsts : IF LPAREN bexp RPAREN LCB line RCB elsests
    elsests : ELSE LCB line RCB | ELSE ifsts | empty

    bexp : bexp andor bexp2 | bexp2
    bexp2 : bexp2 rln exp | exp
    rln : DEQUAL | GTHEN | LTHEN | NOT
    andor : AND | OR

    empty :

    nline : FOR LPAREN fline bexp SCOLON assign RPAREN LCB line RCB
    nline : WHILE LPAREN bexp RPAREN LCB line RCB
    assign : var EQUAL exp



    nline : dtype LBB RBB IDVAR EQUAL arrt SCOLON | STR LBB RBB IDVAR EQUAL arrt SCOLON
    arrt : var | LCB dws RCB
    dws : factarr COM dws | factarr
    factarr : fact | STRING
'''
import sym
import ply.yacc as yacc
from claclex import tokens



vars = {}
pyth = False

# def p_lan_chg(p):
#     '''lan : pyt
#             | line'''
#     if len(p) == 3:
#         p[0] = p[2]
#     else:
#         p[0] = p[1]


def p_line_chg(p):
    '''line : nline line
            | nline'''

def p_nline_init(p):
    '''nline : dtype var SCOLON
                | STR var SCOLON'''
    sym.store(p[2]['value'], p[1])


def p_nline_dec(p):
    'nline : fline'

def p_nline_str(p):
    'nline : STR IDVAR EQUAL strvar SCOLON'
    vars[p[2]] = p[4]

def p_nline_main(p):
    'nline : BOOL MAIN LPAREN RPAREN LCB line RCB'

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


def p_nline_for(p):
    'nline : FOR LPAREN fline bexp SCOLON assign RPAREN sps line RCB'
    sym.remove()


def p_nline_while(p):
    'nline : WHILE LPAREN bexp RPAREN sps  line RCB'
    sym.remove()

def p_sps(p):
    'sps : LCB'
    sym.add_scopes()


def p_ifsts_fst(p):
    'ifsts : IF LPAREN bexp RPAREN LCB line RCB elsests'


def p_elsests_fst(p):
    '''elsests : ELSE LCB line RCB
                | ELSE ifsts
                | empty'''

def p_numexp_stm(p):
    'numexp : assign SCOLON'


def p_exp_pm(p):
    '''exp : exp PLUS term
           | exp MINUS term
           | term'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[1]['type'] == p[3]['type']:
            p[0] = {'value':None, 'type': p[1]['type']}
        else:
            print("type mismatch")
            exit()


def p_term_mdm(p):
    '''term : term MUL fact
            | term DIV fact
            | term MOD fact
            | fact'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[1]['type'] == p[3]['type']:
            p[0] = {'value':None, 'type': p[1]['type']}
        else:
            print("type mismatch")
            exit()


def p_fact_val(p):
    '''fact : INTEGER
            | FLOAT
            | var
            | bval
            | CHAR'''
    if p[1]["type"] == "ID":
        p[0] = sym.lookup(p[1]["value"])
        # print(p[1])
    else:
        p[0] = p[1]


def p_bval_val(p):
    '''bval : TRUE
            | FALSE'''

def p_var_id(p):
    '''var : IDVAR
            | IDVAR LBB INTEGER RBB
            | IDVAR LBB IDVAR RBB'''

    p[0] = p[1]

def p_dtype_num(p):
    '''dtype : INT
            | FLT
            | CHR
            | BOOL'''
    p[0] = p[1]

def p_strvar_val(p):
    '''strvar : STRING
            | var'''

def p_bexp_fst(p):
    '''bexp : bexp andor bexp2
            | bexp2'''

def p_bexp2_fst(p):
    '''bexp2 : bexp2 rln exp
            | exp'''

def p_rln_fst(p):
    '''rln : DEQUAL
            | GTHEN
            | LTHEN
            | NOT'''

def p_andor_fst(p):
    '''andor : AND
            | OR'''

def p_empty(p):
    'empty :'
    pass

def p_assign_num(p):
    'assign : var EQUAL exp'
    p[1] = sym.lookup(p[1]["value"])
    if p[1]["type"] == p[3]["type"]:
        pass
    else:
        print("type mismatch")
        exit()


def p_fline_for(p):
    '''fline : dtype numexp
            | numexp'''


def p_nline_arr(p):
    '''nline : dtype LBB RBB IDVAR EQUAL arrt SCOLON
                | STR LBB RBB IDVAR EQUAL arrt SCOLON'''

def p_arrt_data(p):
    '''arrt : var
            | LCB dws RCB'''

def p_dws_vals(p):
    '''dws : factarr COM dws
            | factarr'''

def p_factarr_vals(p):
    '''factarr : fact
    | STRING'''


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    print(p)

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

data = '''int a;
        int b;
       '''


'''
int[] arr = {1,"df",23, true, 12.32, 'w',asdf};
int as[2];
int[] asdf = {12};
string[] a1 = {1,2,3};

boolean main(){
if(a[0]==a[1]){
for(int a=1; b>2; b=b+1){
    a[4]=1;
}
}}
'''




'''
boolean main(){
if(a==a){
for(int a=1; b>2; b=b+1){
    a=1;
}
while(a>d<as<asdf>1<2 and a!1==df<2.34>'1' or true or false){
    a=1;
}
 }else{
    if(b < a and c == b){
        string ayush = "ayush";
    }else if(b ! c){
        b = c;
        }
}
string z;
print(a+b*4-6/23%2);
# return();
return(true);
exit();
}

'''

#
#
# '''
''' 
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
# int a = "ajsb";
char ch = '5';
string res;
'''
result = parser.parse(data)
print(result)