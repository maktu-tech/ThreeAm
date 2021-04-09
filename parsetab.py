
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL CHAR CHR COM COMMENT DEQUAL DIV ELSE EQUAL EXIT FALSE FLOAT FLT FOR GTHEN IDVAR IF INT INTEGER LBB LCB LPAREN LTHEN MAIN MINUS MOD MUL NOT OR PLUS PRINT RBB RCB RETURN RPAREN SCOLON STR STRING TRUE VOID WHILE WITHline : nline line \n            | nlinenline : dtype var SCOLON  \n             | STR var SCOLONnline : dtype numexp \n             | numexpnline : STR var EQUAL strvar SCOLONnline : BOOL MAIN LPAREN RPAREN LCB line RCBnline : RETURN LPAREN bval RPAREN SCOLONnline : ifstsnline : EXIT LPAREN RPAREN SCOLONnline : PRINT LPAREN nline RPAREN SCOLONnline : FOR LPAREN nline bexp SCOLON nline RPAREN LCB line RCBnline : WHILE LPAREN bexp RPAREN LCB line RCBifsts : IF LPAREN bexp RPAREN LCB line RCB elsestselsests : ELSE LCB line RCB \n                | ELSE ifsts \n                | emptynumexp : var EQUAL exp SCOLONexp : exp PLUS term \n           | exp MINUS term \n           | termterm : term MUL fact \n            | term DIV fact \n            | term MOD fact \n            | factfact : INTEGER \n            | FLOAT \n            | var\n            | bval\n            | CHARbval : TRUE\n            | FALSEvar : IDVARdtype : INT \n            | FLT \n            | CHR \n            | BOOLstrvar : STRING \n            | varbexp : bexp andor bexp2 \n            | bexp2bexp2 : bexp2 rln exp \n            | exprln : DEQUAL \n            | GTHEN \n            | LTHEN \n            | NOTandor : AND \n            | ORempty :'
    
_lr_action_items = {'STR':([0,2,6,9,21,27,28,31,42,53,64,82,83,84,85,86,87,90,95,97,98,99,100,102,104,105,106,108,],[5,5,-6,-10,-5,5,5,-3,-4,-19,-11,-7,5,-9,-12,5,5,5,-8,-14,-51,5,-15,-18,5,-17,-13,-16,]),'BOOL':([0,2,6,9,21,27,28,31,42,53,64,82,83,84,85,86,87,90,95,97,98,99,100,102,104,105,106,108,],[7,7,-6,-10,-5,7,7,-3,-4,-19,-11,-7,7,-9,-12,7,7,7,-8,-14,-51,7,-15,-18,7,-17,-13,-16,]),'RETURN':([0,2,6,9,21,27,28,31,42,53,64,82,83,84,85,86,87,90,95,97,98,99,100,102,104,105,106,108,],[8,8,-6,-10,-5,8,8,-3,-4,-19,-11,-7,8,-9,-12,8,8,8,-8,-14,-51,8,-15,-18,8,-17,-13,-16,]),'EXIT':([0,2,6,9,21,27,28,31,42,53,64,82,83,84,85,86,87,90,95,97,98,99,100,102,104,105,106,108,],[10,10,-6,-10,-5,10,10,-3,-4,-19,-11,-7,10,-9,-12,10,10,10,-8,-14,-51,10,-15,-18,10,-17,-13,-16,]),'PRINT':([0,2,6,9,21,27,28,31,42,53,64,82,83,84,85,86,87,90,95,97,98,99,100,102,104,105,106,108,],[11,11,-6,-10,-5,11,11,-3,-4,-19,-11,-7,11,-9,-12,11,11,11,-8,-14,-51,11,-15,-18,11,-17,-13,-16,]),'FOR':([0,2,6,9,21,27,28,31,42,53,64,82,83,84,85,86,87,90,95,97,98,99,100,102,104,105,106,108,],[12,12,-6,-10,-5,12,12,-3,-4,-19,-11,-7,12,-9,-12,12,12,12,-8,-14,-51,12,-15,-18,12,-17,-13,-16,]),'WHILE':([0,2,6,9,21,27,28,31,42,53,64,82,83,84,85,86,87,90,95,97,98,99,100,102,104,105,106,108,],[13,13,-6,-10,-5,13,13,-3,-4,-19,-11,-7,13,-9,-12,13,13,13,-8,-14,-51,13,-15,-18,13,-17,-13,-16,]),'INT':([0,2,6,9,21,27,28,31,42,53,64,82,83,84,85,86,87,90,95,97,98,99,100,102,104,105,106,108,],[14,14,-6,-10,-5,14,14,-3,-4,-19,-11,-7,14,-9,-12,14,14,14,-8,-14,-51,14,-15,-18,14,-17,-13,-16,]),'FLT':([0,2,6,9,21,27,28,31,42,53,64,82,83,84,85,86,87,90,95,97,98,99,100,102,104,105,106,108,],[15,15,-6,-10,-5,15,15,-3,-4,-19,-11,-7,15,-9,-12,15,15,15,-8,-14,-51,15,-15,-18,15,-17,-13,-16,]),'CHR':([0,2,6,9,21,27,28,31,42,53,64,82,83,84,85,86,87,90,95,97,98,99,100,102,104,105,106,108,],[16,16,-6,-10,-5,16,16,-3,-4,-19,-11,-7,16,-9,-12,16,16,16,-8,-14,-51,16,-15,-18,16,-17,-13,-16,]),'IF':([0,2,6,9,21,27,28,31,42,53,64,82,83,84,85,86,87,90,95,97,98,99,100,101,102,104,105,106,108,],[17,17,-6,-10,-5,17,17,-3,-4,-19,-11,-7,17,-9,-12,17,17,17,-8,-14,-51,17,-15,17,-18,17,-17,-13,-16,]),'IDVAR':([0,2,3,5,6,7,9,14,15,16,21,22,27,28,29,30,31,42,43,48,53,54,55,56,57,58,64,68,69,70,71,72,73,74,75,82,83,84,85,86,87,90,95,97,98,99,100,102,104,105,106,108,],[18,18,18,18,-6,-38,-10,-35,-36,-37,-5,18,18,18,18,18,-3,-4,18,18,-19,18,18,18,18,18,-11,18,-49,-50,18,-45,-46,-47,-48,-7,18,-9,-12,18,18,18,-8,-14,-51,18,-15,-18,18,-17,-13,-16,]),'$end':([1,2,6,9,19,21,31,42,53,64,82,84,85,95,97,98,100,102,105,106,108,],[0,-2,-6,-10,-1,-5,-3,-4,-19,-11,-7,-9,-12,-8,-14,-51,-15,-18,-17,-13,-16,]),'RCB':([2,6,9,19,21,31,42,53,64,82,84,85,91,93,94,95,97,98,100,102,103,105,106,107,108,],[-2,-6,-10,-1,-5,-3,-4,-19,-11,-7,-9,-12,95,97,98,-8,-14,-51,-15,-18,106,-17,-13,108,-16,]),'EQUAL':([4,18,20,23,],[22,-34,22,43,]),'RPAREN':([6,9,18,21,26,31,32,34,35,36,37,38,39,40,41,42,44,45,47,49,50,51,52,53,64,77,78,79,80,81,82,84,85,88,89,92,95,97,98,100,102,105,106,108,],[-6,-10,-34,-5,46,-3,-29,-22,-26,-27,-28,-30,-31,-32,-33,-4,62,63,65,67,-42,-44,76,-19,-11,-20,-21,-23,-24,-25,-7,-9,-12,-41,-43,96,-8,-14,-51,-15,-18,-17,-13,-16,]),'INTEGER':([6,9,21,22,29,30,31,42,48,53,54,55,56,57,58,64,68,69,70,71,72,73,74,75,82,84,85,95,97,98,100,102,105,106,108,],[-6,-10,-5,36,36,36,-3,-4,36,-19,36,36,36,36,36,-11,36,-49,-50,36,-45,-46,-47,-48,-7,-9,-12,-8,-14,-51,-15,-18,-17,-13,-16,]),'FLOAT':([6,9,21,22,29,30,31,42,48,53,54,55,56,57,58,64,68,69,70,71,72,73,74,75,82,84,85,95,97,98,100,102,105,106,108,],[-6,-10,-5,37,37,37,-3,-4,37,-19,37,37,37,37,37,-11,37,-49,-50,37,-45,-46,-47,-48,-7,-9,-12,-8,-14,-51,-15,-18,-17,-13,-16,]),'CHAR':([6,9,21,22,29,30,31,42,48,53,54,55,56,57,58,64,68,69,70,71,72,73,74,75,82,84,85,95,97,98,100,102,105,106,108,],[-6,-10,-5,39,39,39,-3,-4,39,-19,39,39,39,39,39,-11,39,-49,-50,39,-45,-46,-47,-48,-7,-9,-12,-8,-14,-51,-15,-18,-17,-13,-16,]),'TRUE':([6,9,21,22,25,29,30,31,42,48,53,54,55,56,57,58,64,68,69,70,71,72,73,74,75,82,84,85,95,97,98,100,102,105,106,108,],[-6,-10,-5,40,40,40,40,-3,-4,40,-19,40,40,40,40,40,-11,40,-49,-50,40,-45,-46,-47,-48,-7,-9,-12,-8,-14,-51,-15,-18,-17,-13,-16,]),'FALSE':([6,9,21,22,25,29,30,31,42,48,53,54,55,56,57,58,64,68,69,70,71,72,73,74,75,82,84,85,95,97,98,100,102,105,106,108,],[-6,-10,-5,41,41,41,41,-3,-4,41,-19,41,41,41,41,41,-11,41,-49,-50,41,-45,-46,-47,-48,-7,-9,-12,-8,-14,-51,-15,-18,-17,-13,-16,]),'MAIN':([7,],[24,]),'LPAREN':([8,10,11,12,13,17,24,],[25,26,27,28,29,30,44,]),'SCOLON':([18,20,23,32,33,34,35,36,37,38,39,40,41,46,50,51,59,60,61,63,65,66,77,78,79,80,81,88,89,],[-34,31,42,-29,53,-22,-26,-27,-28,-30,-31,-32,-33,64,-42,-44,-40,82,-39,84,85,86,-20,-21,-23,-24,-25,-41,-43,]),'MUL':([18,32,34,35,36,37,38,39,40,41,77,78,79,80,81,],[-34,-29,56,-26,-27,-28,-30,-31,-32,-33,56,56,-23,-24,-25,]),'DIV':([18,32,34,35,36,37,38,39,40,41,77,78,79,80,81,],[-34,-29,57,-26,-27,-28,-30,-31,-32,-33,57,57,-23,-24,-25,]),'MOD':([18,32,34,35,36,37,38,39,40,41,77,78,79,80,81,],[-34,-29,58,-26,-27,-28,-30,-31,-32,-33,58,58,-23,-24,-25,]),'PLUS':([18,32,33,34,35,36,37,38,39,40,41,51,77,78,79,80,81,89,],[-34,-29,54,-22,-26,-27,-28,-30,-31,-32,-33,54,-20,-21,-23,-24,-25,54,]),'MINUS':([18,32,33,34,35,36,37,38,39,40,41,51,77,78,79,80,81,89,],[-34,-29,55,-22,-26,-27,-28,-30,-31,-32,-33,55,-20,-21,-23,-24,-25,55,]),'DEQUAL':([18,32,34,35,36,37,38,39,40,41,50,51,77,78,79,80,81,88,89,],[-34,-29,-22,-26,-27,-28,-30,-31,-32,-33,72,-44,-20,-21,-23,-24,-25,72,-43,]),'GTHEN':([18,32,34,35,36,37,38,39,40,41,50,51,77,78,79,80,81,88,89,],[-34,-29,-22,-26,-27,-28,-30,-31,-32,-33,73,-44,-20,-21,-23,-24,-25,73,-43,]),'LTHEN':([18,32,34,35,36,37,38,39,40,41,50,51,77,78,79,80,81,88,89,],[-34,-29,-22,-26,-27,-28,-30,-31,-32,-33,74,-44,-20,-21,-23,-24,-25,74,-43,]),'NOT':([18,32,34,35,36,37,38,39,40,41,50,51,77,78,79,80,81,88,89,],[-34,-29,-22,-26,-27,-28,-30,-31,-32,-33,75,-44,-20,-21,-23,-24,-25,75,-43,]),'AND':([18,32,34,35,36,37,38,39,40,41,49,50,51,52,66,77,78,79,80,81,88,89,],[-34,-29,-22,-26,-27,-28,-30,-31,-32,-33,69,-42,-44,69,69,-20,-21,-23,-24,-25,-41,-43,]),'OR':([18,32,34,35,36,37,38,39,40,41,49,50,51,52,66,77,78,79,80,81,88,89,],[-34,-29,-22,-26,-27,-28,-30,-31,-32,-33,70,-42,-44,70,70,-20,-21,-23,-24,-25,-41,-43,]),'STRING':([43,],[61,]),'LCB':([62,67,76,96,101,],[83,87,90,99,104,]),'ELSE':([98,],[101,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'line':([0,2,83,87,90,99,104,],[1,19,91,93,94,103,107,]),'nline':([0,2,27,28,83,86,87,90,99,104,],[2,2,47,48,2,92,2,2,2,2,]),'dtype':([0,2,27,28,83,86,87,90,99,104,],[3,3,3,3,3,3,3,3,3,3,]),'var':([0,2,3,5,22,27,28,29,30,43,48,54,55,56,57,58,68,71,83,86,87,90,99,104,],[4,4,20,23,32,4,4,32,32,59,32,32,32,32,32,32,32,32,4,4,4,4,4,4,]),'numexp':([0,2,3,27,28,83,86,87,90,99,104,],[6,6,21,6,6,6,6,6,6,6,6,]),'ifsts':([0,2,27,28,83,86,87,90,99,101,104,],[9,9,9,9,9,9,9,9,9,105,9,]),'exp':([22,29,30,48,68,71,],[33,51,51,51,51,89,]),'term':([22,29,30,48,54,55,68,71,],[34,34,34,34,77,78,34,34,]),'fact':([22,29,30,48,54,55,56,57,58,68,71,],[35,35,35,35,35,35,79,80,81,35,35,]),'bval':([22,25,29,30,48,54,55,56,57,58,68,71,],[38,45,38,38,38,38,38,38,38,38,38,38,]),'bexp':([29,30,48,],[49,52,66,]),'bexp2':([29,30,48,68,],[50,50,50,88,]),'strvar':([43,],[60,]),'andor':([49,52,66,],[68,68,68,]),'rln':([50,88,],[71,71,]),'elsests':([98,],[100,]),'empty':([98,],[102,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> line","S'",1,None,None,None),
  ('line -> nline line','line',2,'p_line_chg','clacyacc.py',53),
  ('line -> nline','line',1,'p_line_chg','clacyacc.py',54),
  ('nline -> dtype var SCOLON','nline',3,'p_nline_init','clacyacc.py',57),
  ('nline -> STR var SCOLON','nline',3,'p_nline_init','clacyacc.py',58),
  ('nline -> dtype numexp','nline',2,'p_nline_dec','clacyacc.py',64),
  ('nline -> numexp','nline',1,'p_nline_dec','clacyacc.py',65),
  ('nline -> STR var EQUAL strvar SCOLON','nline',5,'p_nline_str','clacyacc.py',68),
  ('nline -> BOOL MAIN LPAREN RPAREN LCB line RCB','nline',7,'p_nline_main','clacyacc.py',72),
  ('nline -> RETURN LPAREN bval RPAREN SCOLON','nline',5,'p_nline_ret','clacyacc.py',75),
  ('nline -> ifsts','nline',1,'p_nline_if','clacyacc.py',78),
  ('nline -> EXIT LPAREN RPAREN SCOLON','nline',4,'p_nline_exit','clacyacc.py',81),
  ('nline -> PRINT LPAREN nline RPAREN SCOLON','nline',5,'p_nline_print','clacyacc.py',84),
  ('nline -> FOR LPAREN nline bexp SCOLON nline RPAREN LCB line RCB','nline',10,'p_nline_for','clacyacc.py',87),
  ('nline -> WHILE LPAREN bexp RPAREN LCB line RCB','nline',7,'p_nline_while','clacyacc.py',90),
  ('ifsts -> IF LPAREN bexp RPAREN LCB line RCB elsests','ifsts',8,'p_ifsts_fst','clacyacc.py',93),
  ('elsests -> ELSE LCB line RCB','elsests',4,'p_elsests_fst','clacyacc.py',96),
  ('elsests -> ELSE ifsts','elsests',2,'p_elsests_fst','clacyacc.py',97),
  ('elsests -> empty','elsests',1,'p_elsests_fst','clacyacc.py',98),
  ('numexp -> var EQUAL exp SCOLON','numexp',4,'p_numexp_stm','clacyacc.py',101),
  ('exp -> exp PLUS term','exp',3,'p_exp_pm','clacyacc.py',106),
  ('exp -> exp MINUS term','exp',3,'p_exp_pm','clacyacc.py',107),
  ('exp -> term','exp',1,'p_exp_pm','clacyacc.py',108),
  ('term -> term MUL fact','term',3,'p_term_mdm','clacyacc.py',111),
  ('term -> term DIV fact','term',3,'p_term_mdm','clacyacc.py',112),
  ('term -> term MOD fact','term',3,'p_term_mdm','clacyacc.py',113),
  ('term -> fact','term',1,'p_term_mdm','clacyacc.py',114),
  ('fact -> INTEGER','fact',1,'p_fact_val','clacyacc.py',117),
  ('fact -> FLOAT','fact',1,'p_fact_val','clacyacc.py',118),
  ('fact -> var','fact',1,'p_fact_val','clacyacc.py',119),
  ('fact -> bval','fact',1,'p_fact_val','clacyacc.py',120),
  ('fact -> CHAR','fact',1,'p_fact_val','clacyacc.py',121),
  ('bval -> TRUE','bval',1,'p_bval_val','clacyacc.py',124),
  ('bval -> FALSE','bval',1,'p_bval_val','clacyacc.py',125),
  ('var -> IDVAR','var',1,'p_var_id','clacyacc.py',128),
  ('dtype -> INT','dtype',1,'p_dtype_num','clacyacc.py',132),
  ('dtype -> FLT','dtype',1,'p_dtype_num','clacyacc.py',133),
  ('dtype -> CHR','dtype',1,'p_dtype_num','clacyacc.py',134),
  ('dtype -> BOOL','dtype',1,'p_dtype_num','clacyacc.py',135),
  ('strvar -> STRING','strvar',1,'p_strvar_val','clacyacc.py',138),
  ('strvar -> var','strvar',1,'p_strvar_val','clacyacc.py',139),
  ('bexp -> bexp andor bexp2','bexp',3,'p_bexp_fst','clacyacc.py',142),
  ('bexp -> bexp2','bexp',1,'p_bexp_fst','clacyacc.py',143),
  ('bexp2 -> bexp2 rln exp','bexp2',3,'p_bexp2_fst','clacyacc.py',146),
  ('bexp2 -> exp','bexp2',1,'p_bexp2_fst','clacyacc.py',147),
  ('rln -> DEQUAL','rln',1,'p_rln_fst','clacyacc.py',150),
  ('rln -> GTHEN','rln',1,'p_rln_fst','clacyacc.py',151),
  ('rln -> LTHEN','rln',1,'p_rln_fst','clacyacc.py',152),
  ('rln -> NOT','rln',1,'p_rln_fst','clacyacc.py',153),
  ('andor -> AND','andor',1,'p_andor_fst','clacyacc.py',156),
  ('andor -> OR','andor',1,'p_andor_fst','clacyacc.py',157),
  ('empty -> <empty>','empty',0,'p_empty','clacyacc.py',160),
]
