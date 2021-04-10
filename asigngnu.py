def printTab(tbl,clm):
    print('',end='\t')
    for e in clm:
        if(len(e)==8):
            print(e,end='')
        else:
            print(e,end ='\t')
    print()
    rn = 0
    for row in tbl:
        print(rn,end='\t')
        rn+=1
        for cell in row:
            print(cell,end='\t')
        print()

def accp(tbl):
    for i in range(len(tbl[1])):
        tbl[1][i] = 'acpt'

class State:
    def __init__(self,rstr):
        self.rawStr = rstr
        self.sft = {}
        self.rds = {}

        self.stsno(self.rawStr[0])
        j = self.gen_items(self.rawStr[1:])
        if(j<len(self.rawStr)):
            self.fillsr(self.rawStr[j+1:])

    def stsno(self,s):
        t = s.split()
        self.sno = int(t[-1])

    def gen_items(self,s):
        j = 0
        self.items = []
        l = len(s)
        while(j<l and s[j][0] == '('):
            self.items.append(' '.join(s[j].split()[1:]))
            j+=1
        return j

    def fillsr(self,s):

        for e in s:
            t = e.split()
            if(t[1] == 'shift'):
                self.sft[t[0]] = t[-1]
            else:
                self.rds[t[0]] = t[4]

f = open('parser.out')
data = f.read().split('\n')
temp = []
for i in range(len(data)):
    data[i] = data[i].strip()
    if(len(data[i]) != 0):
        temp.append(data[i])
data = temp
temp = []


i = 0
while(data[i][:4] != 'Rule'):
    i+=1

data = data[i:]

i = 0
rules = []
while(data[i][:4] == 'Rule'):
    rules.append(' '.join(data[i].split()[2:]))
    i+=1

data = data[i+1:]

terminals = []

i = 0
while(data[i][:5] != 'error'):
    terminals.append(data[i].split()[0])
    i+=1
terminals.append('$end')
data = data[i+2:]

i = 0
nonterminals = []
while(data[i][:7] != 'Parsing'):
    nonterminals.append(data[i].split()[0])
    i+=1

data = data[i+1:]

sts = []
temp = [data[0]]

for e in data[1:]:
    if(e[:5] == 'state'):
        sts.append(State(temp))
        temp = []

    temp.append(e)
sts.append(State(temp))

# for s in sts:
#     print(s.sno)
#     print(s.items)
#     print(s.rds)
#     print(s.sft)
#     print('\n\n')
# print(nonterminals)


table = []
# tecount = len(terminals)+len(nonterminals)

for s in sts:
    row = []
    skeys = list(s.sft.keys()) 
    rkeys = list(s.rds.keys())
    for ter in terminals:
        if(ter in skeys):
            row.append(s.sft[ter])
        elif(ter in rkeys):
            row.append('r'+s.rds[ter])
        else:
            row.append('-')

    for nter in nonterminals:
        if(nter in skeys):
            row.append(s.sft[nter])
        elif(nter in rkeys):
            row.append('r'+s.rds[nter])
        else:
            row.append('-')
    
    table.append(row)
accp(table)
printTab(table,(terminals+nonterminals))