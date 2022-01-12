n = int(input())
d = list(map(int,input().split()))
d.sort()
i = n // 2 - 1
ans = d[i+1] - d[i]
print(ans)