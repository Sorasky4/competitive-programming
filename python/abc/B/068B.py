n = int(input())
cnt = 0
ans = 1
for i in range(1,n+1):
    tmp = 0
    while i % 2 == 0:
        tmp += 1
        i //= 2
    if cnt < tmp:
        cnt = tmp
        ans = i * 2 ** tmp
print(ans)