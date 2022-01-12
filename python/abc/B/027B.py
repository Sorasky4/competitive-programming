n = int(input())
a = [int(i) for i in input().split()]
if sum(a) % n != 0:
    print(-1)
else:
    ave = sum(a) // n
    v = [0] * (n + 1)
    for i in range(n):
        v[i+1] = v[i]
        v[i+1] += a[i]
    ans = 0
    for i in range(1,n):
        if v[i] != i * ave:
            ans += 1
    print(ans)