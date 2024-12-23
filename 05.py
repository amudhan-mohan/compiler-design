import re

class Prod:
    def __init__(self, name, products):
        self.name = name
        self.products = products
        self.first = []
        self.follow = []

def is_terminal(s):
    if re.match(re.compile('^[A-Z]$'), s):
        return False
    else:
        return True

# Find production by name
def find_prod(name):
    for x in p:
        if x.name == name:
            return x

def first(name):
    for x in p:
        if name == x.name:
            return x.first

def follow(name):
    for x in p:
        if name == x.name:
            return x.follow

def calc_first():
    for i in reversed(range(len(p))):
        for x in p[i].products:
            if is_terminal(x[0]):
                p[i].first.append(x[0])
            else:
                f = find_prod(x[0]).first
                p[i].first.extend(f)
                c = 1
                while 'e' in f:
                    if c == len(x):  # Stop if we've processed all symbols
                        break
                    if is_terminal(x[c]):
                        f = x[c]
                    else:
                        f = find_prod(x[c]).first
                    p[i].first.extend(f)
                    c += 1
        p[i].first = list(set(p[i].first))

def calc_follow():
    p[0].follow.append('$')  # Add $ to follow of start symbol
    for x in p:
        find_follow(x)

def find_follow(x):
    for y in p:
        for pr in y.products:
            for c in range(len(pr)):
                if pr[c] == x.name:
                    if c + 1 >= len(pr):  # Last symbol in production
                        x.follow.extend(y.follow)
                    elif is_terminal(pr[c + 1]):
                        x.follow.append(pr[c + 1])
                    elif 'e' not in first(pr[c + 1]):
                        x.follow.extend(first(pr[c + 1]))
                    elif follow(pr[c + 1]):
                        x.follow.extend(first(pr[c + 1]) + follow(pr[c + 1]))
                    else:
                        x.follow.extend(first(pr[c + 1]) + find_follow(find_prod(pr[c + 1])))
    x.follow = list(set(x.follow) - {'e'})
    return x.follow

# Input grammar
p = []
n = int(input("No of production: "))
print("Epsilon = e")
for i in range(n):
    ip = input(f"Production {i + 1}: ")
    name, prods = ip.split(' -> ')
    products = prods.split(' | ')
    p.append(Prod(name, products))

# Calculate first and follow
calc_first()
calc_follow()

# Print first and follow sets
for x in p:
    print(f'first({x.name}) = {x.first}')
for x in p:
    print(f'follow({x.name}) = {x.follow}')
