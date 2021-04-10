# ------------------------------------------------------------
# 
# data_type: int(INT), char(CHR), string(STR), float(FLT), array, bool(BOOL), 
# keyword: print, exit, (include), for, with, while, if - else, {continue}, {break}, and, or, true, false, return
# arthmetic operator "-"|"*"|"+"|"/"|"%"(MOD)
# rln operator "=="(DEQUAL) | "!"(not equal to)(NOT) | ">"(GTHEN) | "<"(LTHEN)
# assignment "=" (EQUAL)
# separator [(LBB) ](RBB) ((LPAREN) )(RPAREN) {(LCB) }(RCB) ,(COM) ;(SCOLON)
# number (INTEGER)
# floating number (FLOAT)
# string (STRING)
# variable (IDVAR)
# comments #
# ------------------------------------------------------------

 
import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'INT',
   'FLT',
   'STR',
   'CHR',
   'EQUAL',
   'SCOLON',
   'BOOL',
   'TRUE',
   'FALSE',
   'INTEGER',
   'FLOAT',
   'STRING',
   'CHAR',
   'IDVAR',
   'LBB',
   'RBB',
   'LCB',
   'RCB',
   'LPAREN',
   'RPAREN',
   'PRINT',
   'EXIT',
   'COM',
   'FOR',
   'WHILE',
   'WITH',
   'IF',
   'ELSE',
   'AND',
   'OR',
   'PLUS',
   'MINUS',
   'MUL',
   'DIV',
   'MOD',
   'DEQUAL',
   'NOT',
   'LTHEN',
   'GTHEN',
   'COMMENT',
   'MAIN',
   'VOID',
   'RETURN'
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MUL   = r'\*'
t_DIV  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQUAL   = r'='
t_SCOLON = r';'
t_MOD = r'%'
t_DEQUAL = r'=='
t_NOT = r'!'
t_GTHEN = r'>'
t_LTHEN = r'<'
t_RBB = r'\]'
t_LBB = r'\['
t_RCB = r'}'
t_LCB = r'{'
t_COM = r','


def t_INT(t):
    r'int'
    return t

def t_MAIN(t):
    r'main'
    return t

def t_VOID(t):
    r'void'
    return t

def t_CHR(t):
    r'char'
    return t

def t_STR(t):
    r'string'
    return t

def t_BOOL(t):
    r'boolean'
    return t

def t_FLT(t):
    r'float'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_EXIT(t):
    r'exit'
    return t

def t_FOR(t):
    r'for'
    return t

def t_WITH(t):
    r'with'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_AND(t):
    r'and'
    return t

def t_OR(t):
    r'or'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_TRUE(t):
    r'true'
    t.value = 1
    return t

def t_FALSE(t):
    r'false'
    t.value = 0
    return t

def t_IDVAR(t):
    r'[_a-zA-Z][_a-zA-Z0-9]*'
    return t

# A regular expression rule with some action code

def t_FLOAT(t):
    r'[+-]?[0-9]+\.[0-9]+'
    t.value = float(t.value)    
    return t


def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_CHAR(t):
    r'\'([^\\\n]|(\\.))*?\''
    if(len(t.value) == 2):
        print("InValid Char")
    t.value = ord(t.value[-2])
    return t


# C or C++ comment (ignore)    
def t_COMMENT(t):
    r'\#.*'
    pass

 # C string
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\n'

# Error handlingf rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
 # Test it out
# data = '''
# int[] a = {4,5,6};
# < > + [] () { } ; 12.23 if else print exit 
# 12Sds 
# _1 %1
# 1false
# "ayush agarwal"
# '''

# data = 'int ayu = 45;'
# # Give the lexer some input
# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)