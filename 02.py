import re

t = 0
f = 1

def nodret(ip):
    global t, f
    e = u'\u03b5'
    nodes = []

    if re.match(r'^[a-z]$', ip):
        nodes = [
            (t, t + 1, ip)
        ]
        t += 1
    elif re.match(r'^[a-z]\*$', ip):
        nodes = [
            (t, t + 1, e),
            (t, t + 3, e),
            (t + 1, t + 2, ip[0]),
            (t + 2, t + 1, e),
            (t + 2, t + 3, e)
        ]
        t += 3
    elif re.match(r'^[a-z]\/[a-z]$', ip):
        nodes = [
            (t, t + 1, e),
            (t, t + 3, e),
            (t + 1, t + 2, ip[0]),
            (t + 3, t + 4, ip[2]),
            (t + 2, t + 5, e),
            (t + 4, t + 5, e),
        ]
        t += 5
    else:
        print("Please enter basic expressions (linear combination of a, a*, a/b, a b)")
        f = 0
    return nodes

def tab_gen(v):
    ips = list(set([e for e1, e2, e in v]))
    ips.sort()
    a = [[[] for j in range(len(ips))] for i in range(t)]
    
    # Fill the transition table
    for s, d, i in v:
        a[s][ips.index(i)].append(d)
    
    print('State', end="")
    for x in ips:
        print(f'\t{x}', end='')
    print('\n', '-' * (len(ips) * 10))

    for i in range(t):
        print(f'{i}', end='')
        for j in range(len(ips)):
            print(f'\t{a[i][j]}', end='')
        print()

    print(f'State {t} is the final state')

ip = input("Enter regex (leave space between characters): ")
nodes = []
for ch in ip.split():
    nodes += nodret(ch)

if f:
    tab_gen(nodes)
