#ビット全探索

n,m = map(int,input().split())
a = sorted([int(i) for i in input().split()])
ans = -10**18
for i in range(2**n):
    cmb = 1
    for j in range(n):
        if ((i >> j) & 1):
            cmb *= a[j]
    if 1 in a:
        ans = cmb if abs(m - ans) > abs(m - cmb) else ans
    else:
        if cmb != 1:
            ans = cmb if abs(m - ans) > abs(m - cmb) else ans
print(ans)