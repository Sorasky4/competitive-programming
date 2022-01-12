import collections
n = int(input())
m,l= map(int,input().split())
p = list(map(int,input().split()))
cnt = [0]*n
for i in range(m):
    p[i] -= 1
    if p[i] + l + 1 <= len(cnt):
        for j in range(p[i],p[i]+l+1):
            cnt[j] += 1
    else:
        for j in range(p[i],len(cnt)):
            cnt[j] += 1
    if p[i] - l >= 0:
        for j in range(p[i]-l,p[i]):
            cnt[j] += 1
    else:
        for j in range(0,p[i]):
            cnt[j] += 1
print(cnt.count(1))