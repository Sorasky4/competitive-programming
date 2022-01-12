n = int(input())
a = list(map(int,input().split()))
po = 0
ne = 0
for i in range(n):
    if a[i] >= 0:
        po += a[i]
    else:
        ne += a[i]
print(po)
print(ne)