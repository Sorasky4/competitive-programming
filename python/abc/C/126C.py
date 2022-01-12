'''
def half(n):
    return n / 2

n,k=map(int,input().split())
cnt = [1/n]*n
ans = 0
if n >= k:
    ans += sum(cnt[k-1:])
    cnt = [1/n]*(k-1)
if n != k:
    cnt = list(map(half,cnt))
while k > 1:
    a = k
    k /= 2
    a //= 2
    if n <= a:
        cnt = list(map(half,cnt))
    else:
        ans += sum(cnt[int(a):])
        cnt = list(map(half,cnt[:int(a)]))
ans += sum(cnt)
print(ans)
'''

n,k=map(int,input().split())
ans = 0
for i in range(1,n+1):
    tmp = 1/n
    while i < k:
        i *= 2
        tmp /= 2
    ans += tmp
print(ans)