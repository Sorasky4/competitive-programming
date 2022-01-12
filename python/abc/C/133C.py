l,r = map(int,input().split())
ans = 2018
flag = 0
for i in range(l,r):
    for j in range(l+1,r+1):
        ans = min(ans,i*j%2019)
        if ans == 0:
            flag = 1
            break
    if flag:
        break
print(ans)