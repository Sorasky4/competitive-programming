n,m,X,Y = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
for i in range(X+1,Y+1):
    for j in range(n):
        if i <= x[j]:
            break
    else:
        for k in range(m):
            if y[k] < i:
                break
        else:
            print('No War')
            break
else:
    print('War')