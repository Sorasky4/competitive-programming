n = int(input())
a = sorted(list(map(int,input().split())),reverse=True)
w = 0
h = 0
for i in range(n-1):
    if a[i] == a[i+1] and w == 0:
        w = a[i]
        a[i+1] = 0
    if a[i] == a[i+1] and w != 0:
        h = a[i]
        break
if w == 0 or h == 0:
    ans = 0
else:
    ans = int(h*w)
print(ans)