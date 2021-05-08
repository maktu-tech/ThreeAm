stk = [{}]

def add_scope():
    stk.append({})

def remove_scope():
    stk.pop()

def store(name,tpe,value=None,lineNo=0, arraytype = None):

    for st in stk:
        if(name in st):
            print('ERROR(line no.: {}): Already Declared'.format(lineNo))
            exit()
    stk[-1][name] = {'type': tpe, 'value': value, 'line': lineNo}
    if(arraytype):
        stk[-1][name]['arraytype'] = arraytype 

def lookup(name):
    for st in stk[::-1]:
        if(name in st):
            return st[name]        
    print(name,'not Declared')
    exit()

def update_spe(name,fields,values):

    for st in stk:
        if name in st:
            for i in range(len(fields)):
                st[name][fields[i]] = values[i]
            return
    print(name+ " not declared")
    exit()

def lookup_init(name):
    for st in stk[::-1]:
        if(name in st):
            return st[name]        
    return None