st = {}

def store(name,tpe,value=None,lineNo=0):
    if(name not in st):
        st[name] = {'type': tpe, 'value': value, 'line': lineNo}
    else:
        print('ERROR(line no.: {}): Already Declared'.format(lineNo))

def lookup(name):
    if(name in st):
        return st[name]
    else:
        print(name,'not Declared')