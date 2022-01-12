n, m = map(int,input().split())
l = [0]*m
r = [0]*m
for i in range(m):
    l1,r1 = map(int,input().split())
    l[i] = l1
    r[i] = r1
print(max(min(r) - max(l) + 1, 0))