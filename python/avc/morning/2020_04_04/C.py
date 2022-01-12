n, m = map(int, input().split())
if n == 1:
    a = 0
    b = 10
else:
    a = 10**(n-1)
    b = 10**n
s = []
c = []
for i in range(m):
    ss, cc = map(int,input().split())
    s.append(ss)
    c.append(cc)
for i in range(a,b):
    ans = str(i)
    for j in range(m):
        if ans[s[j]-1] != str(c[j]):
            break
    else:
        print(ans)
        exit()
else:
    print(-1)