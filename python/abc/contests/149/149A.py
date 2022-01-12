x = [i for i in input().split()]
x[0],x[1] = x[1],x[0]
print(''.join(map(str,x)))