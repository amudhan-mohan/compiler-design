# import re

# p = []

# class Prod:
#     def __init__(self, name, products):
#         self.name = name
#         self.products = products
#         self.first = []
#         self.follow = []

# def is_terminal(s):
#     if re.match(re.compile('^[A-Z]$'), s):
#         return False
#     else:
#         return True

# # Find production by name:
# def find_prod(name):
#     for x in p:
#         if x.name == name:
#             return x

# def first(name):
#     for x in p:
#         if name == x.name:
#             return x.first

# def follow(name):
#     for x in p:
#         if name == x.name:
#             return x.follow

# def calc_first():
#     for i in reversed(range(len(p))):
#         for x in p[i].products:
#             if is_terminal(x[0]):
#                 p[i].first.append(x[0])
#             else:
#                 f = find_prod(x[0]).first
#                 p[i].first.extend(f)
#                 c = 1
#                 while 'e' in f:
#                     if is_terminal(x[c]):
#                         f = x[c]
#                     else:
#                         f = find_prod(x[c]).first
#                     p[i].first.extend(f)
#                     c += 1
#                     if c == len(x):
#                         break
#         p[i].first = list(set(p[i].first))

# def calc_follow():
#     p[0].follow.append('$')
#     for x in p:
#         find_follow(x)

# def find_follow(x):
#     for y in p:
#         for pr in y.products:
#             for c in range(len(pr)):
#                 if pr[c] == x.name:
#                     if c + 1 >= len(pr):
#                         x.follow.extend(y.follow)
#                     elif is_terminal(pr[c + 1]):
#                         x.follow.append(pr[c + 1])
#                     elif 'e' not in first(pr[c + 1]):
#                         x.follow.extend(first(pr[c + 1]))
#                     elif follow(pr[c + 1]):
#                         x.follow.extend(first(pr[c + 1]) + follow(pr[c + 1]))
#                     else:
#                         x.follow.extend(first(pr[c + 1]) + find_follow(find_prod(pr[c + 1])))
#                     x.follow = list(set(x.follow) - {'e'})
#     return x.follow

# n = int(input("No of production: "))
# print("Epsilon = e")
# for i in range(n):
#     ip = input(f"Production {i + 1}: ")
#     name, prods = ip.split(' -> ')
#     products = prods.split(' | ')
#     p.append(Prod(name, products))

# calc_first()
# calc_follow()

# # Print First and Follow sets
# for x in p:
#     print(f'first({x.name}) = {x.first}')
# for x in p:
#     print(f'follow({x.name}) = {x.follow}')



# import re

# # Class to hold the production rules and associated First and Follow sets
# class Prod:
#     def __init__(self, name, products):
#         self.name = name
#         self.products = products
#         self.first = []  # First set
#         self.follow = []  # Follow set

# # Helper function to check if a symbol is a terminal (lowercase)
# def is_terminal(s):
#     return not re.match(r'^[A-Z]$', s)

# # Function to find a production by its name
# def find_prod(name):
#     for prod in p:
#         if prod.name == name:
#             return prod

# # Function to calculate the First set for all productions
# def calc_first():
#     # Initial first set population
#     for prod in p:
#         for x in prod.products:
#             for symbol in x:
#                 if is_terminal(symbol):  # If it's a terminal, add to First
#                     prod.first.append(symbol)
#                     break
#                 else:  # If it's a non-terminal, add First of that non-terminal
#                     prod.first.extend(find_prod(symbol).first)
#                     if 'e' not in find_prod(symbol).first:
#                         break
#     # Remove duplicates and 'e' from First sets
#     for prod in p:
#         prod.first = list(set(prod.first))

# # Function to calculate the Follow set for all productions
# def calc_follow():
#     p[0].follow.append('$')  # Add end-of-input symbol to the follow set of the start symbol
#     for prod in p:
#         find_follow(prod)

# # Function to find the Follow set for a specific production
# def find_follow(x):
#     for y in p:
#         for pr in y.products:
#             for c in range(len(pr)):
#                 if pr[c] == x.name:
#                     if c + 1 >= len(pr):  # If this is the last symbol in the production
#                         x.follow.extend(y.follow)
#                     elif is_terminal(pr[c + 1]):  # If the next symbol is a terminal
#                         x.follow.append(pr[c + 1])
#                     else:  # If the next symbol is a non-terminal
#                         f = first(pr[c + 1])
#                         if 'e' in f:  # If the next symbol can derive epsilon
#                             f.remove('e')
#                             x.follow.extend(f + y.follow)
#                         else:
#                             x.follow.extend(f)
#     x.follow = list(set(x.follow) - {'e'})  # Remove epsilon from follow set

# # Function to get the First set for a symbol
# def first(symbol):
#     if is_terminal(symbol):
#         return [symbol]
#     else:
#         return find_prod(symbol).first

# # Input grammar and production rules
# n = int(input("No of productions: "))
# print("Epsilon is represented by 'e'.")
# p = []

# for i in range(n):
#     ip = input(f"Production {i + 1}: ")
#     name, prods = ip.split(' -> ')
#     products = prods.split(' | ')
#     p.append(Prod(name, products))

# # Calculate First and Follow sets
# calc_first()
# calc_follow()

# # Output the results
# for prod in p:
#     print(f'first({prod.name}) = {prod.first}')
    
# for prod in p:
#     print(f'follow({prod.name}) = {prod.follow}')



# import re

# # Class to represent a production rule and store its First and Follow sets
# class Prod:
#     def __init__(self, name, products):
#         self.name = name
#         self.products = products
#         self.first = []  # First set
#         self.follow = []  # Follow set

# # Helper function to check if a symbol is a terminal
# def is_terminal(s):
#     return not re.match(r'^[A-Z]$', s)

# # Function to find a production by its name
# def find_prod(name):
#     for x in p:
#         if x.name == name:
#             return x

# # Function to calculate the First sets for all productions
# def calc_first():
#     # For each production, calculate the First set
#     for i in reversed(range(len(p))):  # Process productions in reverse order
#         for x in p[i].products:
#             f = []
#             for symbol in x:
#                 if is_terminal(symbol):  # If it's a terminal, add to the First set
#                     f.append(symbol)
#                     break
#                 else:  # If it's a non-terminal, add the First set of that non-terminal
#                     prod = find_prod(symbol)
#                     f.extend(prod.first)
#                     if 'e' not in prod.first:  # Stop if epsilon ('e') is not in First set
#                         break
#             p[i].first = list(set(p[i].first) | set(f))

# # Function to calculate the Follow sets for all productions
# def calc_follow():
#     p[0].follow.append('$')  # Add the end-of-input symbol to the follow set of the start symbol
#     for x in p:
#         find_follow(x)

# # Function to calculate the Follow set for a specific production
# def find_follow(x):
#     for y in p:
#         for pr in y.products:
#             for c in range(len(pr)):
#                 if pr[c] == x.name:  # If the non-terminal is found in the right-hand side
#                     if c + 1 >= len(pr):  # If it's the last symbol, add the Follow set of the parent
#                         x.follow.extend(y.follow)
#                     elif is_terminal(pr[c + 1]):  # If the next symbol is a terminal, add it to Follow
#                         x.follow.append(pr[c + 1])
#                     else:  # If the next symbol is a non-terminal, add its First set
#                         f = first(pr[c + 1])
#                         if 'e' in f:  # If the next symbol can derive epsilon, propagate Follow sets
#                             f.remove('e')
#                             x.follow.extend(f + y.follow)
#                         else:
#                             x.follow.extend(f)
#     x.follow = list(set(x.follow) - {'e'})  # Remove epsilon from the follow set

# # Function to get the First set for a symbol (non-terminal or terminal)
# def first(symbol):
#     if is_terminal(symbol):
#         return [symbol]
#     else:
#         return find_prod(symbol).first

# # Main function to input grammar and calculate First and Follow sets
# n = int(input("No of production: "))
# print("Epsilon = e")

# # List to store productions
# p = []

# # Input grammar and create production rules
# for i in range(n):
#     ip = input(f"Production {i + 1}: ")
#     name, prods = ip.split(' -> ')
#     products = prods.split(' | ')
#     p.append(Prod(name, products))

# # Calculate First and Follow sets
# calc_first()
# calc_follow()

# # Print the First and Follow sets for each non-terminal
# for x in p:
#     print(f'first({x.name}) = {x.first}')
    
# for x in p:
#     print(f'follow({x.name}) = {x.follow}')



# import re

# # Class to represent a production rule and store its First and Follow sets
# class Prod:
#     def __init__(self, name, products):
#         self.name = name
#         self.products = products
#         self.first = []  # First set
#         self.follow = []  # Follow set

# # Helper function to check if a symbol is a terminal
# def is_terminal(s):
#     return not re.match(r'^[A-Z]$', s)

# # Function to find a production by its name
# def find_prod(name):
#     for x in p:
#         if x.name == name:
#             return x

# # Function to calculate the First sets for all productions
# def calc_first():
#     # For each production, calculate the First set
#     for i in range(len(p)):  # Process productions in order
#         for x in p[i].products:
#             f = []
#             for symbol in x:
#                 if is_terminal(symbol):  # If it's a terminal, add to the First set
#                     f.append(symbol)
#                     break
#                 else:  # If it's a non-terminal, add the First set of that non-terminal
#                     prod = find_prod(symbol)
#                     f.extend(prod.first)
#                     if 'e' not in prod.first:  # Stop if epsilon ('e') is not in First set
#                         break
#             p[i].first = list(set(p[i].first) | set(f))

# # Function to calculate the Follow sets for all productions
# def calc_follow():
#     p[0].follow.append('$')  # Add the end-of-input symbol to the follow set of the start symbol
#     for x in p:
#         find_follow(x)

# # Function to calculate the Follow set for a specific production
# def find_follow(x):
#     for y in p:
#         for pr in y.products:
#             for c in range(len(pr)):
#                 if pr[c] == x.name:  # If the non-terminal is found in the right-hand side
#                     if c + 1 >= len(pr):  # If it's the last symbol, add the Follow set of the parent
#                         x.follow.extend(y.follow)
#                     elif is_terminal(pr[c + 1]):  # If the next symbol is a terminal, add it to Follow
#                         x.follow.append(pr[c + 1])
#                     else:  # If the next symbol is a non-terminal, add its First set
#                         f = first(pr[c + 1])
#                         if 'e' in f:  # If the next symbol can derive epsilon, propagate Follow sets
#                             f.remove('e')
#                             x.follow.extend(f + y.follow)
#                         else:
#                             x.follow.extend(f)
#     x.follow = list(set(x.follow) - {'e'})  # Remove epsilon from the follow set

# # Function to get the First set for a symbol (non-terminal or terminal)
# def first(symbol):
#     if is_terminal(symbol):
#         return [symbol]
#     else:
#         return find_prod(symbol).first

# # Main function to input grammar and calculate First and Follow sets
# n = int(input("No of production: "))
# print("Epsilon = e")

# # List to store productions
# p = []

# # Input grammar and create production rules
# for i in range(n):
#     ip = input(f"Production {i + 1}: ")
#     name, prods = ip.split(' -> ')
#     products = prods.split(' | ')
#     p.append(Prod(name, products))

# # Calculate First and Follow sets
# calc_first()
# calc_follow()

# # Print the First and Follow sets for each non-terminal, sorted alphabetically
# for x in p:
#     print(f'first({x.name}) = {sorted(x.first)}')

# for x in p:
#     print(f'follow({x.name}) = {sorted(x.follow)}')



import re
p=[]
class Prod:
    def __init__(self, name, products):
        self.name=name
        self.products=products
        self.first=[]
        self.follow=[]
def is_terminal(s):
    if re.match(re.compile('^[A-Z]$'),s):
        return False
    else:
        return True
#find production by name:
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
                c=1
                while 'e' in f:
                    if is_terminal(x[c]):
                        f=x[c]
                    else:
                        f=find_prod(x[c]).first
                    p[i].first.extend(f)
                    c+=1
                    if c == len(x):
                        break
        p[i].first = list(set(p[i].first))
def calc_follow():
    p[0].follow.append('$')
    for x in p:
        find_follow(x)
def find_follow(x):
    for y in p:
        for pr in y.products:
            for c in range(len(pr)):
                if pr[c] == x.name:
                    if c+1 >= len(pr):
                        x.follow.extend(y.follow)
                    elif is_terminal(pr[c+1]):
                        x.follow.append(pr[c+1])
                    elif 'e' not in first(pr[c+1]):
                        x.follow.extend(first(pr[c+1]))
                    elif follow(pr[c+1]):
                        x.follow.extend(first(pr[c+1]) + follow(pr[c+1]))
                    else:
                        x.follow.extend(first(pr[c+1]) + find_follow(find_prod(pr[c+1])))
                    x.follow = list(set(x.follow)-{'e'})
        return x.follow
n = int(input("No of production: "))
print("Epsilon = e")
for i in range(n):
    ip = input(f"Production {i+1}: ")
    name, prods = ip.split(' -> ')
    products = prods.split(' | ')
    p.append(Prod(name, products))

calc_first()
calc_follow()

#print first and follow
for x in p:
    print(f'first({x.name}) = {x.first}')
for x in p:
    print(f'follow({x.name}) = {x.follow}')