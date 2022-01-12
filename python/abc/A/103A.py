a = list(map(int,input().split()))
if a[0] == a[1] and a[1] == a[2]:
    print(0)
else:
    print(max(a[0],a[1],a[2]) - min(a[0],a[1],a[2]))