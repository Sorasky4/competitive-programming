a,b,k = map(int,input().split())
flag = 0
cnt = 0
ans = 0
for i in range(101,0,-1):
    if a % i == 0 and b % i == 0:
        cnt += 1
        if cnt == k:
            ans = i
            flag = 1
    if flag:
        break
print(ans)