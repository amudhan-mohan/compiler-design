gram = {
"S": ["S+S", "S*S",'S-S','(S)', "id"]
}
start = "S"
inp = "(id+id)$"
stack = "$"
print(f'{"Stack": <15}' + "|" + f'{"Input Buffer": <15}' + "|" + 'Parsing Action')
print(f'{"-":-<50}')
while True:
    i = 0
    for i in range (len(gram[start])):
        if gram[start][i] in stack:
            stack = stack.replace(gram[start][i], start)
            print(f'{stack: <15}' + "|" + f'{inp: <15}' + "|" + f'Reduce > {gram[start][i]}')
    if len(inp) > 1:
        stack += inp[0]
        inp = inp[1:]
        print(f'{stack: <15}' + "|" + f'{inp: <15}' + "|" + 'Shift')
    if stack == ("$" + start):
        if inp == '$':
            print(f'{stack: <15}' + "|" + f'{inp: <15}' + "|" + 'Accepted')
        else:
            print(f'{stack: <15}' + "|" + f'{inp: <15}' + "|" + 'Rejected')
        break