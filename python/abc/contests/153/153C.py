n, k = map(int,input().split())
h = sorted([int(i) for i in input().split()], reverse=True)

for i in range(min(k,n)):
    h[i] = 0
print(sum(h))