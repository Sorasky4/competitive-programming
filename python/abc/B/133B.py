'''n,d=map(int,input().split())
x = [list(map(int,input().split())) for i in range(n)]
count = 0
for i in range(n-1):
    for j in range(d-1):
        a = ((x[i][j]-x[i+1][j])**2 + (x[i][j+1]-x[i+1][j+1])**2)**(1/2)
        print(a)
        if a == int(a):
            count += 1
    
#for k in range(d-1):
#    b = ((x[n][k]-x[0][k])**2 + (x[n][k+1]-x[0][k+1])**2)**(1/2)
#if b == int(b):
#    count += 1
#print(count)

#さっぱりわからん 
ここから下、2019/09/19'''
n,d = map(int,input().split())
x = [list(map(int,input().split())) for i in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1,n):
        norm = 0
        for k in range(d):
            diff = abs(x[i][k] - x[j][k])
            norm += diff**2
        flag = 0
        for k in range(norm+1):
            if k**2 == norm:
                flag = 1
        if flag:
            ans += 1
print(ans)