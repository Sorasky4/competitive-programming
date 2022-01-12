'''
WA
n,k = map(int,input().split())
a = [i for i in input().split()]
one = a.index('1')
ans = 0
if n == k:
    ans = 1
elif one <= k//2:
    ans += 1
    for _ in range(one+k//2,n,k-1):
        ans += 1
elif n - k//2 - 1 <= one:
    ans += 1
    for _ in range(one-k//2,-1,-(k-1)):
        ans += 1
else:
    for _ in range(one,n,k-1):
        ans += 1
    for _ in range(one-1,-1,-(k-1)):
        ans += 1
print(ans)
'''