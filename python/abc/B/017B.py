x = input()
ans = 'YES'
if len(x) == 1:
    if x!='o'and x!='k'and x!='u':
        ans = 'NO'
else:
    for i in range(len(x)-1):
        if x[i]!='c'and x[i]!='h'and x[i]!='o'and x[i]!='k'and x[i]!='u':
            ans = 'NO'
        elif x[i] == 'c':
            if x[i+1] != 'h':
                ans = 'NO'
    for i in range(len(x)-1,0,-1):
        if x[i]!='c'and x[i]!='h'and x[i]!='o'and x[i]!='k'and x[i]!='u':
            ans = 'NO'
        elif x[i] == 'h':
            if x[i-1] != 'c':
                ans = 'NO'
    if x[0] == 'h' or x[-1] == 'c':
        ans = 'NO'
print(ans)