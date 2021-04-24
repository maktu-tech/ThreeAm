
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL CHAR CHR COM COMMENT DEQUAL DIV ELSE EQUAL EXIT FALSE FLOAT FLT FOR GTHEN IDVAR IF INT INTEGER LBB LCB LPAREN LTHEN MAIN MINUS MOD MUL NOT OR PLUS PRINT RBB RCB RETURN RPAREN SCOLON STR STRING TRUE VOID WHILE WITHline : nline line \n            | nlinenline : dtype var SCOLON\n                | STR var SCOLONnline : flinenline : STR IDVAR EQUAL strvar SCOLONnline : BOOL MAIN LPAREN RPAREN lcb line rcbnline : RETURN LPAREN bval RPAREN SCOLONnline : ifstsnline : EXIT LPAREN RPAREN SCOLONnline : PRINT LPAREN pline RPAREN SCOLONpline : exp\n            | STRINGnline : FOR LPAREN fline bexp SCOLON assign RPAREN lcb line rcbnline : WHILE LPAREN bexp RPAREN lcb line rcbifsts : IF LPAREN bexp RPAREN lcb line rcb elsestsrcb : RCBlcb : LCBelsests : ELSE lcb line rcb \n                | ELSE ifsts\n                | emptynumexp : assign SCOLONexp : exp PLUS term \n           | exp MINUS term \n           | termterm : term MUL fact\n            | term DIV fact\n            | term MOD fact\n            | factfact : INTEGER \n            | FLOAT \n            | varval\n            | bval\n            | CHARvarval : var\n              | var LBB exp RBBbval : TRUE\n            | FALSEvar : IDVARdtype : INT \n            | FLT \n            | CHR \n            | BOOLstrvar : STRING \n            | varvalbexp : bexp andor bexp2 \n            | bexp2bexp2 : bexp2 rln exp \n            | exprln : DEQUAL \n            | GTHEN \n            | LTHEN \n            | NOTandor : AND \n            | ORempty :assign : varval EQUAL exp\n              | varval EQUAL STRINGfline : dtype numexp \n            | numexpnline : dtype LBB RBB IDVAR EQUAL arrt SCOLON\n                | STR LBB RBB IDVAR EQUAL arrt SCOLONarrt : var \n            | LCB dws RCBdws : factarr COM dws \n            | factarrfactarr : fact \n    | STRING'
    
_lr_action_items = {'STR':([0,2,6,10,19,25,35,39,51,82,101,103,104,105,106,108,111,120,125,126,127,129,130,133,134,136,139,140,141,143,],[5,5,-5,-9,-60,-59,-22,-3,-4,-10,-6,5,-18,-8,-11,5,5,-61,-62,-7,-17,-15,-56,5,-16,-21,5,-20,-14,-19,]),'BOOL':([0,2,6,10,19,25,34,35,39,51,82,101,103,104,105,106,108,111,120,125,126,127,129,130,133,134,136,139,140,141,143,],[8,8,-5,-9,-60,-59,62,-22,-3,-4,-10,-6,8,-18,-8,-11,8,8,-61,-62,-7,-17,-15,-56,8,-16,-21,8,-20,-14,-19,]),'RETURN':([0,2,6,10,19,25,35,39,51,82,101,103,104,105,106,108,111,120,125,126,127,129,130,133,134,136,139,140,141,143,],[9,9,-5,-9,-60,-59,-22,-3,-4,-10,-6,9,-18,-8,-11,9,9,-61,-62,-7,-17,-15,-56,9,-16,-21,9,-20,-14,-19,]),'EXIT':([0,2,6,10,19,25,35,39,51,82,101,103,104,105,106,108,111,120,125,126,127,129,130,133,134,136,139,140,141,143,],[11,11,-5,-9,-60,-59,-22,-3,-4,-10,-6,11,-18,-8,-11,11,11,-61,-62,-7,-17,-15,-56,11,-16,-21,11,-20,-14,-19,]),'PRINT':([0,2,6,10,19,25,35,39,51,82,101,103,104,105,106,108,111,120,125,126,127,129,130,133,134,136,139,140,141,143,],[12,12,-5,-9,-60,-59,-22,-3,-4,-10,-6,12,-18,-8,-11,12,12,-61,-62,-7,-17,-15,-56,12,-16,-21,12,-20,-14,-19,]),'FOR':([0,2,6,10,19,25,35,39,51,82,101,103,104,105,106,108,111,120,125,126,127,129,130,133,134,136,139,140,141,143,],[13,13,-5,-9,-60,-59,-22,-3,-4,-10,-6,13,-18,-8,-11,13,13,-61,-62,-7,-17,-15,-56,13,-16,-21,13,-20,-14,-19,]),'WHILE':([0,2,6,10,19,25,35,39,51,82,101,103,104,105,106,108,111,120,125,126,127,129,130,133,134,136,139,140,141,143,],[15,15,-5,-9,-60,-59,-22,-3,-4,-10,-6,15,-18,-8,-11,15,15,-61,-62,-7,-17,-15,-56,15,-16,-21,15,-20,-14,-19,]),'INT':([0,2,6,10,19,25,34,35,39,51,82,101,103,104,105,106,108,111,120,125,126,127,129,130,133,134,136,139,140,141,143,],[16,16,-5,-9,-60,-59,16,-22,-3,-4,-10,-6,16,-18,-8,-11,16,16,-61,-62,-7,-17,-15,-56,16,-16,-21,16,-20,-14,-19,]),'FLT':([0,2,6,10,19,25,34,35,39,51,82,101,103,104,105,106,108,111,120,125,126,127,129,130,133,134,136,139,140,141,143,],[17,17,-5,-9,-60,-59,17,-22,-3,-4,-10,-6,17,-18,-8,-11,17,17,-61,-62,-7,-17,-15,-56,17,-16,-21,17,-20,-14,-19,]),'CHR':([0,2,6,10,19,25,34,35,39,51,82,101,103,104,105,106,108,111,120,125,126,127,129,130,133,134,136,139,140,141,143,],[18,18,-5,-9,-60,-59,18,-22,-3,-4,-10,-6,18,-18,-8,-11,18,18,-61,-62,-7,-17,-15,-56,18,-16,-21,18,-20,-14,-19,]),'IF':([0,2,6,10,19,25,35,39,51,82,101,103,104,105,106,108,111,120,125,126,127,129,130,133,134,135,136,139,140,141,143,],[20,20,-5,-9,-60,-59,-22,-3,-4,-10,-6,20,-18,-8,-11,20,20,-61,-62,-7,-17,-15,-56,20,-16,20,-21,20,-20,-14,-19,]),'IDVAR':([0,2,3,5,6,8,10,16,17,18,19,25,26,33,34,35,36,37,38,39,40,51,52,53,60,61,62,71,72,73,74,75,82,86,87,88,89,90,91,92,93,95,101,102,103,104,105,106,107,108,111,114,120,125,126,127,129,130,132,133,134,136,139,140,141,143,],[7,7,7,28,-5,-43,-9,-40,-41,-42,-60,-59,7,7,7,-22,7,7,7,-3,69,-4,7,79,7,7,-43,7,7,7,7,7,-10,7,-54,-55,7,-50,-51,-52,-53,7,-6,7,7,-18,-8,-11,7,7,7,7,-61,-62,-7,-17,-15,-56,7,7,-16,-21,7,-20,-14,-19,]),'$end':([1,2,6,10,19,22,25,35,39,51,82,101,105,106,120,125,126,127,129,130,134,136,140,141,143,],[0,-2,-5,-9,-60,-1,-59,-22,-3,-4,-10,-6,-8,-11,-61,-62,-7,-17,-15,-56,-16,-21,-20,-14,-19,]),'RCB':([2,4,6,7,10,19,22,25,35,39,44,45,46,47,48,49,50,51,70,82,101,105,106,116,118,119,120,121,122,123,124,125,126,127,129,130,134,136,137,138,140,141,142,143,],[-2,-35,-5,-39,-9,-60,-1,-59,-22,-3,-30,-31,-32,-33,-34,-37,-38,-4,-36,-10,-6,-8,-11,127,127,127,-61,131,-66,-67,-68,-62,-7,-17,-15,-56,-16,-21,-65,127,-20,-14,127,-19,]),'LBB':([3,4,5,7,8,16,17,18,23,],[24,26,29,-39,-43,-40,-41,-42,26,]),'EQUAL':([4,7,21,23,28,69,70,79,],[-35,-39,38,-35,52,95,-36,102,]),'MUL':([4,7,42,43,44,45,46,47,48,49,50,70,96,97,98,99,100,],[-35,-39,73,-29,-30,-31,-32,-33,-34,-37,-38,-36,73,73,-26,-27,-28,]),'DIV':([4,7,42,43,44,45,46,47,48,49,50,70,96,97,98,99,100,],[-35,-39,74,-29,-30,-31,-32,-33,-34,-37,-38,-36,74,74,-26,-27,-28,]),'MOD':([4,7,42,43,44,45,46,47,48,49,50,70,96,97,98,99,100,],[-35,-39,75,-29,-30,-31,-32,-33,-34,-37,-38,-36,75,75,-26,-27,-28,]),'RBB':([4,7,24,29,41,42,43,44,45,46,47,48,49,50,70,96,97,98,99,100,],[-35,-39,40,53,70,-25,-29,-30,-31,-32,-33,-34,-37,-38,-36,-23,-24,-26,-27,-28,]),'PLUS':([4,7,41,42,43,44,45,46,47,48,49,50,58,65,67,70,96,97,98,99,100,110,],[-35,-39,71,-25,-29,-30,-31,-32,-33,-34,-37,-38,71,71,71,-36,-23,-24,-26,-27,-28,71,]),'MINUS':([4,7,41,42,43,44,45,46,47,48,49,50,58,65,67,70,96,97,98,99,100,110,],[-35,-39,72,-25,-29,-30,-31,-32,-33,-34,-37,-38,72,72,72,-36,-23,-24,-26,-27,-28,72,]),'RPAREN':([4,7,32,42,43,44,45,46,47,48,49,50,54,55,57,58,59,63,64,65,66,67,68,70,96,97,98,99,100,109,110,117,],[-35,-39,56,-25,-29,-30,-31,-32,-33,-34,-37,-38,80,81,83,-12,-13,85,-47,-49,94,-57,-58,-36,-23,-24,-26,-27,-28,-46,-48,128,]),'DEQUAL':([4,7,42,43,44,45,46,47,48,49,50,64,65,70,96,97,98,99,100,109,110,],[-35,-39,-25,-29,-30,-31,-32,-33,-34,-37,-38,90,-49,-36,-23,-24,-26,-27,-28,90,-48,]),'GTHEN':([4,7,42,43,44,45,46,47,48,49,50,64,65,70,96,97,98,99,100,109,110,],[-35,-39,-25,-29,-30,-31,-32,-33,-34,-37,-38,91,-49,-36,-23,-24,-26,-27,-28,91,-48,]),'LTHEN':([4,7,42,43,44,45,46,47,48,49,50,64,65,70,96,97,98,99,100,109,110,],[-35,-39,-25,-29,-30,-31,-32,-33,-34,-37,-38,92,-49,-36,-23,-24,-26,-27,-28,92,-48,]),'NOT':([4,7,42,43,44,45,46,47,48,49,50,64,65,70,96,97,98,99,100,109,110,],[-35,-39,-25,-29,-30,-31,-32,-33,-34,-37,-38,93,-49,-36,-23,-24,-26,-27,-28,93,-48,]),'AND':([4,7,42,43,44,45,46,47,48,49,50,63,64,65,66,70,84,96,97,98,99,100,109,110,],[-35,-39,-25,-29,-30,-31,-32,-33,-34,-37,-38,87,-47,-49,87,-36,87,-23,-24,-26,-27,-28,-46,-48,]),'OR':([4,7,42,43,44,45,46,47,48,49,50,63,64,65,66,70,84,96,97,98,99,100,109,110,],[-35,-39,-25,-29,-30,-31,-32,-33,-34,-37,-38,88,-47,-49,88,-36,88,-23,-24,-26,-27,-28,-46,-48,]),'SCOLON':([4,7,14,23,27,28,42,43,44,45,46,47,48,49,50,56,64,65,67,68,70,76,77,78,81,83,84,96,97,98,99,100,109,110,112,113,115,131,],[-35,-39,35,39,51,-39,-25,-29,-30,-31,-32,-33,-34,-37,-38,82,-47,-49,-57,-58,-36,101,-44,-45,105,106,107,-23,-24,-26,-27,-28,-46,-48,120,-63,125,-64,]),'COM':([4,7,44,45,46,47,48,49,50,70,122,123,124,],[-35,-39,-30,-31,-32,-33,-34,-37,-38,-36,132,-67,-68,]),'MAIN':([8,],[30,]),'LPAREN':([9,11,12,13,15,20,30,],[31,32,33,34,36,37,54,]),'INTEGER':([19,25,26,33,35,36,37,38,60,71,72,73,74,75,86,87,88,89,90,91,92,93,114,132,],[-60,-59,44,44,-22,44,44,44,44,44,44,44,44,44,44,-54,-55,44,-50,-51,-52,-53,44,44,]),'FLOAT':([19,25,26,33,35,36,37,38,60,71,72,73,74,75,86,87,88,89,90,91,92,93,114,132,],[-60,-59,45,45,-22,45,45,45,45,45,45,45,45,45,45,-54,-55,45,-50,-51,-52,-53,45,45,]),'CHAR':([19,25,26,33,35,36,37,38,60,71,72,73,74,75,86,87,88,89,90,91,92,93,114,132,],[-60,-59,48,48,-22,48,48,48,48,48,48,48,48,48,48,-54,-55,48,-50,-51,-52,-53,48,48,]),'TRUE':([19,25,26,31,33,35,36,37,38,60,71,72,73,74,75,86,87,88,89,90,91,92,93,114,132,],[-60,-59,49,49,49,-22,49,49,49,49,49,49,49,49,49,49,-54,-55,49,-50,-51,-52,-53,49,49,]),'FALSE':([19,25,26,31,33,35,36,37,38,60,71,72,73,74,75,86,87,88,89,90,91,92,93,114,132,],[-60,-59,50,50,50,-22,50,50,50,50,50,50,50,50,50,50,-54,-55,50,-50,-51,-52,-53,50,50,]),'STRING':([33,38,52,114,132,],[59,68,77,124,124,]),'LCB':([80,85,94,95,102,128,135,],[104,104,104,114,114,104,104,]),'ELSE':([127,130,],[-17,135,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'line':([0,2,103,108,111,133,139,],[1,22,116,118,119,138,142,]),'nline':([0,2,103,108,111,133,139,],[2,2,2,2,2,2,2,]),'dtype':([0,2,34,103,108,111,133,139,],[3,3,61,3,3,3,3,3,]),'var':([0,2,3,5,26,33,34,36,37,38,52,60,61,71,72,73,74,75,86,89,95,102,103,107,108,111,114,132,133,139,],[4,4,23,27,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,113,113,4,4,4,4,4,4,4,4,]),'fline':([0,2,34,103,108,111,133,139,],[6,6,60,6,6,6,6,6,]),'ifsts':([0,2,103,108,111,133,135,139,],[10,10,10,10,10,10,140,10,]),'assign':([0,2,3,34,61,103,107,108,111,133,139,],[14,14,14,14,14,14,117,14,14,14,14,]),'numexp':([0,2,3,34,61,103,108,111,133,139,],[19,19,25,19,25,19,19,19,19,19,]),'varval':([0,2,3,26,33,34,36,37,38,52,60,61,71,72,73,74,75,86,89,103,107,108,111,114,132,133,139,],[21,21,21,46,46,21,46,46,46,78,46,21,46,46,46,46,46,46,46,21,21,21,21,46,46,21,21,]),'exp':([26,33,36,37,38,60,86,89,],[41,58,65,65,67,65,65,110,]),'term':([26,33,36,37,38,60,71,72,86,89,],[42,42,42,42,42,42,96,97,42,42,]),'fact':([26,33,36,37,38,60,71,72,73,74,75,86,89,114,132,],[43,43,43,43,43,43,43,43,98,99,100,43,43,123,123,]),'bval':([26,31,33,36,37,38,60,71,72,73,74,75,86,89,114,132,],[47,55,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'pline':([33,],[57,]),'bexp':([36,37,60,],[63,66,84,]),'bexp2':([36,37,60,86,],[64,64,64,109,]),'strvar':([52,],[76,]),'andor':([63,66,84,],[86,86,86,]),'rln':([64,109,],[89,89,]),'lcb':([80,85,94,128,135,],[103,108,111,133,139,]),'arrt':([95,102,],[112,115,]),'dws':([114,132,],[121,137,]),'factarr':([114,132,],[122,122,]),'rcb':([116,118,119,138,142,],[126,129,130,141,143,]),'elsests':([130,],[134,]),'empty':([130,],[136,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> line","S'",1,None,None,None),
  ('line -> nline line','line',2,'p_line_chg','clacyacc.py',55),
  ('line -> nline','line',1,'p_line_chg','clacyacc.py',56),
  ('nline -> dtype var SCOLON','nline',3,'p_nline_init','clacyacc.py',59),
  ('nline -> STR var SCOLON','nline',3,'p_nline_init','clacyacc.py',60),
  ('nline -> fline','nline',1,'p_nline_dec','clacyacc.py',64),
  ('nline -> STR IDVAR EQUAL strvar SCOLON','nline',5,'p_nline_str','clacyacc.py',73),
  ('nline -> BOOL MAIN LPAREN RPAREN lcb line rcb','nline',7,'p_nline_main','clacyacc.py',77),
  ('nline -> RETURN LPAREN bval RPAREN SCOLON','nline',5,'p_nline_ret','clacyacc.py',80),
  ('nline -> ifsts','nline',1,'p_nline_if','clacyacc.py',83),
  ('nline -> EXIT LPAREN RPAREN SCOLON','nline',4,'p_nline_exit','clacyacc.py',86),
  ('nline -> PRINT LPAREN pline RPAREN SCOLON','nline',5,'p_nline_print','clacyacc.py',89),
  ('pline -> exp','pline',1,'p_pline_print','clacyacc.py',92),
  ('pline -> STRING','pline',1,'p_pline_print','clacyacc.py',93),
  ('nline -> FOR LPAREN fline bexp SCOLON assign RPAREN lcb line rcb','nline',10,'p_nline_for','clacyacc.py',97),
  ('nline -> WHILE LPAREN bexp RPAREN lcb line rcb','nline',7,'p_nline_while','clacyacc.py',100),
  ('ifsts -> IF LPAREN bexp RPAREN lcb line rcb elsests','ifsts',8,'p_ifsts_fst','clacyacc.py',103),
  ('rcb -> RCB','rcb',1,'p_rcb_scppop','clacyacc.py',106),
  ('lcb -> LCB','lcb',1,'p_lcb_scppush','clacyacc.py',110),
  ('elsests -> ELSE lcb line rcb','elsests',4,'p_elsests_fst','clacyacc.py',114),
  ('elsests -> ELSE ifsts','elsests',2,'p_elsests_fst','clacyacc.py',115),
  ('elsests -> empty','elsests',1,'p_elsests_fst','clacyacc.py',116),
  ('numexp -> assign SCOLON','numexp',2,'p_numexp_stm','clacyacc.py',119),
  ('exp -> exp PLUS term','exp',3,'p_exp_pm','clacyacc.py',123),
  ('exp -> exp MINUS term','exp',3,'p_exp_pm','clacyacc.py',124),
  ('exp -> term','exp',1,'p_exp_pm','clacyacc.py',125),
  ('term -> term MUL fact','term',3,'p_term_mdm','clacyacc.py',144),
  ('term -> term DIV fact','term',3,'p_term_mdm','clacyacc.py',145),
  ('term -> term MOD fact','term',3,'p_term_mdm','clacyacc.py',146),
  ('term -> fact','term',1,'p_term_mdm','clacyacc.py',147),
  ('fact -> INTEGER','fact',1,'p_fact_val','clacyacc.py',170),
  ('fact -> FLOAT','fact',1,'p_fact_val','clacyacc.py',171),
  ('fact -> varval','fact',1,'p_fact_val','clacyacc.py',172),
  ('fact -> bval','fact',1,'p_fact_val','clacyacc.py',173),
  ('fact -> CHAR','fact',1,'p_fact_val','clacyacc.py',174),
  ('varval -> var','varval',1,'p_varval_val','clacyacc.py',178),
  ('varval -> var LBB exp RBB','varval',4,'p_varval_val','clacyacc.py',179),
  ('bval -> TRUE','bval',1,'p_bval_val','clacyacc.py',194),
  ('bval -> FALSE','bval',1,'p_bval_val','clacyacc.py',195),
  ('var -> IDVAR','var',1,'p_var_id','clacyacc.py',199),
  ('dtype -> INT','dtype',1,'p_dtype_num','clacyacc.py',204),
  ('dtype -> FLT','dtype',1,'p_dtype_num','clacyacc.py',205),
  ('dtype -> CHR','dtype',1,'p_dtype_num','clacyacc.py',206),
  ('dtype -> BOOL','dtype',1,'p_dtype_num','clacyacc.py',207),
  ('strvar -> STRING','strvar',1,'p_strvar_val','clacyacc.py',211),
  ('strvar -> varval','strvar',1,'p_strvar_val','clacyacc.py',212),
  ('bexp -> bexp andor bexp2','bexp',3,'p_bexp_fst','clacyacc.py',220),
  ('bexp -> bexp2','bexp',1,'p_bexp_fst','clacyacc.py',221),
  ('bexp2 -> bexp2 rln exp','bexp2',3,'p_bexp2_fst','clacyacc.py',228),
  ('bexp2 -> exp','bexp2',1,'p_bexp2_fst','clacyacc.py',229),
  ('rln -> DEQUAL','rln',1,'p_rln_fst','clacyacc.py',236),
  ('rln -> GTHEN','rln',1,'p_rln_fst','clacyacc.py',237),
  ('rln -> LTHEN','rln',1,'p_rln_fst','clacyacc.py',238),
  ('rln -> NOT','rln',1,'p_rln_fst','clacyacc.py',239),
  ('andor -> AND','andor',1,'p_andor_fst','clacyacc.py',243),
  ('andor -> OR','andor',1,'p_andor_fst','clacyacc.py',244),
  ('empty -> <empty>','empty',0,'p_empty','clacyacc.py',248),
  ('assign -> varval EQUAL exp','assign',3,'p_assign_num','clacyacc.py',252),
  ('assign -> varval EQUAL STRING','assign',3,'p_assign_num','clacyacc.py',253),
  ('fline -> dtype numexp','fline',2,'p_fline_for','clacyacc.py',264),
  ('fline -> numexp','fline',1,'p_fline_for','clacyacc.py',265),
  ('nline -> dtype LBB RBB IDVAR EQUAL arrt SCOLON','nline',7,'p_nline_arr','clacyacc.py',281),
  ('nline -> STR LBB RBB IDVAR EQUAL arrt SCOLON','nline',7,'p_nline_arr','clacyacc.py',282),
  ('arrt -> var','arrt',1,'p_arrt_data','clacyacc.py',291),
  ('arrt -> LCB dws RCB','arrt',3,'p_arrt_data','clacyacc.py',292),
  ('dws -> factarr COM dws','dws',3,'p_dws_vals','clacyacc.py',303),
  ('dws -> factarr','dws',1,'p_dws_vals','clacyacc.py',304),
  ('factarr -> fact','factarr',1,'p_factarr_vals','clacyacc.py',314),
  ('factarr -> STRING','factarr',1,'p_factarr_vals','clacyacc.py',315),
]
