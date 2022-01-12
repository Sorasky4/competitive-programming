n = int(input())
h = [int(i) for i in input().split()]
ans = 0
while sum(h) > 0:
    L = 0
    if 0 not in h:
        ans += 1
        for i in range(n):
            h[i] -= 1
    else:
        for i in range(n):
            if h[i] == 0 and L != i:
                for j in range(L,i):
                    h[j] -= 1
                ans += 1
                L = i + 1
            elif h[L] == 0:
                L += 1
            if i == n-1 and h[i] != 0:
                for j in range(L,n):
                    h[j] -= 1
                ans += 1
print(ans)