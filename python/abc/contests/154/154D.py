n, k = map(int, input().split())
p = [int(i) for i in input().split()]
amax = sum(p[0:k])
bmax = sum(p[0:k])
for i in range(k,n):
    bmax -= p[i-k]
    bmax += p[i]
    amax = max(amax, bmax)
print((amax+k)/2)