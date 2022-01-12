'''RE WA TLE
n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
sa = sorted(a)
sb = sorted(b)
c = [list(i) for i in zip(sb,a)]
cnt = 0
if any(sb[i] < sa[i] for i in range(n)):
    print('No')
    exit(0)
if any(sa[i] <= sb[i-1] for i in range(1,n)):
    print('Yes')
    exit(0)
for i in range(n):
    if c[i][1] != c[i][0]:
        c[i][1],c[c[i][1]-1][1] = c[c[i][1]-1][1],c[i][1] #行列の任意要素だけ交換はできない
        cnt += 1
if cnt <= n-2:
    print('Yes')
else:
    print('No')
'''