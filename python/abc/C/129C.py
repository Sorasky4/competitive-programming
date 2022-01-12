def fibcmb(start,end):
    start += 1
    end -= 1
    up = end - start
    a1 = 1
    a2 = 2
    if up < 0:
        return 0
    elif up == 0:
        return 1
    elif up == 1:
        return a1
    elif up == 2:
        return a2
    else:
        for _ in range(up-2):
            an = a1 + a2
            a1 = a2
            a2 = an
        return an

n,m = map(int,input().split())
a = [int(input()) for _ in range(m)]
ans = 1
cmb = [0]*(m+1)
if m == 0:
    ans = fibcmb(-1,n+1)
else:
    cmb[0] = fibcmb(-1,a[0])
    for i in range(1,m):
        cmb[i] = fibcmb(a[i-1],a[i])
    cmb[-1] = fibcmb(a[-1],n+1)
    for i in range(m+1):
        ans *= cmb[i]
print(ans%1000000007)