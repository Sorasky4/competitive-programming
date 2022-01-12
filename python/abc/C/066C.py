n = int(input())
a = [int(i) for i in input().split()]
ans = []
if n % 2 == 0:
    for i in range(n-1,-1,-2):
        ans.append(a[i])
    for i in range(0,n,2):
        ans.append(a[i])
else:
    for i in range(n-1,-1,-2):
        ans.append(a[i])
    for i in range(1,n,2):
        ans.append(a[i])
print(' '.join(map(str,ans)))