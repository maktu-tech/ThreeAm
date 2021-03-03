
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVIDE EQUAL EXIT IDVAR INTEGER LPAREN MINUS NUMBER PLUS PRINT PYT RPAREN SEMICOLON TIMESlan : pyt\n            | linepyt : PYT linePlineP : nlineP lineP\n            | nlinePnlineP : var EQUAL expressionnlineP : EXIT LPAREN RPARENnlineP : PRINT LPAREN var RPARENline : nline line\n            | nline\n            | pytnline : INTEGER var EQUAL expression SEMICOLONnline : var EQUAL expression SEMICOLONnline : EXIT LPAREN RPAREN SEMICOLONnline : PRINT LPAREN var RPAREN SEMICOLONvar : IDVARexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : term DIVIDE factorterm : factorfactor : NUMBER\n              | varfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'PYT':([0,5,39,45,48,54,],[4,4,-13,-14,-12,-15,]),'INTEGER':([0,5,39,45,48,54,],[6,6,-13,-14,-12,-15,]),'EXIT':([0,4,5,10,12,27,29,30,31,35,36,39,45,47,48,49,50,51,52,53,54,],[8,14,8,-16,14,-24,-19,-22,-23,-6,-7,-13,-14,-8,-12,-17,-18,-20,-21,-25,-15,]),'PRINT':([0,4,5,10,12,27,29,30,31,35,36,39,45,47,48,49,50,51,52,53,54,],[9,15,9,-16,15,-24,-19,-22,-23,-6,-7,-13,-14,-8,-12,-17,-18,-20,-21,-25,-15,]),'IDVAR':([0,4,5,6,10,12,19,21,23,25,26,27,29,30,31,32,35,36,39,40,41,42,43,45,47,48,49,50,51,52,53,54,],[10,10,10,10,-16,10,10,10,10,10,10,-24,-19,-22,-23,10,-6,-7,-13,10,10,10,10,-14,-8,-12,-17,-18,-20,-21,-25,-15,]),'$end':([1,2,3,5,10,11,12,16,17,22,27,29,30,31,35,36,39,45,47,48,49,50,51,52,53,54,],[0,-1,-2,-10,-16,-3,-5,-9,-11,-4,-24,-19,-22,-23,-6,-7,-13,-14,-8,-12,-17,-18,-20,-21,-25,-15,]),'EQUAL':([7,10,13,18,],[19,-16,23,26,]),'LPAREN':([8,9,14,15,19,23,26,32,40,41,42,43,],[20,21,24,25,32,32,32,32,32,32,32,32,]),'TIMES':([10,27,29,30,31,49,50,51,52,53,],[-16,-24,42,-22,-23,42,42,-20,-21,-25,]),'DIVIDE':([10,27,29,30,31,49,50,51,52,53,],[-16,-24,43,-22,-23,43,43,-20,-21,-25,]),'SEMICOLON':([10,27,28,29,30,31,33,38,46,49,50,51,52,53,],[-16,-24,39,-19,-22,-23,45,48,54,-17,-18,-20,-21,-25,]),'PLUS':([10,27,28,29,30,31,35,38,44,49,50,51,52,53,],[-16,-24,40,-19,-22,-23,40,40,40,-17,-18,-20,-21,-25,]),'MINUS':([10,27,28,29,30,31,35,38,44,49,50,51,52,53,],[-16,-24,41,-19,-22,-23,41,41,41,-17,-18,-20,-21,-25,]),'RPAREN':([10,20,24,27,29,30,31,34,37,44,49,50,51,52,53,],[-16,33,36,-24,-19,-22,-23,46,47,53,-17,-18,-20,-21,-25,]),'NUMBER':([19,23,26,32,40,41,42,43,],[31,31,31,31,31,31,31,31,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'lan':([0,],[1,]),'pyt':([0,5,],[2,17,]),'line':([0,5,],[3,16,]),'nline':([0,5,],[5,5,]),'var':([0,4,5,6,12,19,21,23,25,26,32,40,41,42,43,],[7,13,7,18,13,27,34,27,37,27,27,27,27,27,27,]),'lineP':([4,12,],[11,22,]),'nlineP':([4,12,],[12,12,]),'expression':([19,23,26,32,],[28,35,38,44,]),'term':([19,23,26,32,40,41,],[29,29,29,29,49,50,]),'factor':([19,23,26,32,40,41,42,43,],[30,30,30,30,30,30,51,52,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> lan","S'",1,None,None,None),
  ('lan -> pyt','lan',1,'p_lan_chg','clacyacc.py',11),
  ('lan -> line','lan',1,'p_lan_chg','clacyacc.py',12),
  ('pyt -> PYT lineP','pyt',2,'p_pyt_chg','clacyacc.py',19),
  ('lineP -> nlineP lineP','lineP',2,'p_lineP_rep','clacyacc.py',22),
  ('lineP -> nlineP','lineP',1,'p_lineP_rep','clacyacc.py',23),
  ('nlineP -> var EQUAL expression','nlineP',3,'p_nlineP_var','clacyacc.py',27),
  ('nlineP -> EXIT LPAREN RPAREN','nlineP',3,'p_nlineP_exit','clacyacc.py',32),
  ('nlineP -> PRINT LPAREN var RPAREN','nlineP',4,'p_nlineP_print','clacyacc.py',36),
  ('line -> nline line','line',2,'p_line_rep','clacyacc.py',40),
  ('line -> nline','line',1,'p_line_rep','clacyacc.py',41),
  ('line -> pyt','line',1,'p_line_rep','clacyacc.py',42),
  ('nline -> INTEGER var EQUAL expression SEMICOLON','nline',5,'p_nline_var','clacyacc.py',47),
  ('nline -> var EQUAL expression SEMICOLON','nline',4,'p_nline_var_update','clacyacc.py',53),
  ('nline -> EXIT LPAREN RPAREN SEMICOLON','nline',4,'p_nline_exit','clacyacc.py',59),
  ('nline -> PRINT LPAREN var RPAREN SEMICOLON','nline',5,'p_nline_print','clacyacc.py',63),
  ('var -> IDVAR','var',1,'p_var_id','clacyacc.py',67),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','clacyacc.py',75),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','clacyacc.py',79),
  ('expression -> term','expression',1,'p_expression_term','clacyacc.py',83),
  ('term -> term TIMES factor','term',3,'p_term_times','clacyacc.py',87),
  ('term -> term DIVIDE factor','term',3,'p_term_div','clacyacc.py',91),
  ('term -> factor','term',1,'p_term_factor','clacyacc.py',95),
  ('factor -> NUMBER','factor',1,'p_factor_num','clacyacc.py',99),
  ('factor -> var','factor',1,'p_factor_num','clacyacc.py',100),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','clacyacc.py',109),
]
