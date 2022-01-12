n = int(input())
op = []
d = []
v = []
top = 0
for i in range(n):
    op1,d1 = [str(i) for i in input().split()]
    op.append(op1)
    d.append(d1)
for i in range(n):
    if not v and op[i] == 'pop':
        continue
    elif op[i] == 'push':
        v.append(d[i])
        top += 1
    else:
        top -= 1
        v.pop(top)
for i in range(len(v))[::-1]:
    print('stack' + '[' + str(i) + ']' + ' = ' + str(v[i]))