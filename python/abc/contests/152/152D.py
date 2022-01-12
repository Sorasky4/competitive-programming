n = int(input())
ans = 0
cmb = [[0 for _ in range(9)] for _ in range(9)]
if n <= 10:
    print(min(n,9))
    exit(0)
for i in range(1,n+1):
    if str(i)[0] != '0' and str(i)[-1] != '0':
        cmb[int(str(i)[0])-1][int(str(i)[-1])-1] += 1
for i in range(9):
    for j in range(9):
        if cmb[i][j] != 0 and cmb[j][i] != 0:
            ans += (cmb[i][j] * cmb[j][i]) 
print(ans)