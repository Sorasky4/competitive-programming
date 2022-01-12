n = int(input())
a = [int(i) for i in input().split()]
sunuke = a[0]
arai = sum(a) - sunuke
ans = abs(sunuke - arai)
for i in range(1,n-1):
    sunuke += a[i]
    arai -= a[i]
    ans = min(ans,abs(sunuke-arai))
print(ans)