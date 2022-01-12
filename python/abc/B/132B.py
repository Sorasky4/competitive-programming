n = int(input())
p = list(map(int,input().split()))
cnt = 0
for i in range(n-2):
    flag1 = p[i] < p[i+1] and p[i+1] < p[i+2]
    flag2 = p[i+2] < p[i+1] and p[i+1] < p[i]
    if flag1 or flag2:
        cnt += 1
print(cnt)