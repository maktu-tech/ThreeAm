# symbol table
# table { name: {value: ,type: ,line: []}}

stack = [{}]


def add_scopes():
    stack.append({})


def remove():
    stack.pop()


def store(name, type, line=0, value = None):
    if name not in stack[len(stack)-1]:
        stack[len(stack)-1].update({name: {'value': value, 'type': type, 'line': line}})
        print(stack[len(stack)-1])
    else:
        print("Already declared")
        exit()


def lookup(name1):
    for x in range(len(stack)-1, -1, -1):
        if name1 in stack[x]:
            # print(stack[x][name1])
            return stack[x][name1]

    print(name1 + " not declared")
    exit()

