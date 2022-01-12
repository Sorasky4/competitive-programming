n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse=True)
cnt = 0
if n == 1:
    a[0] //= 2**m
elif n == 2:
    while m > 0:
        a[0] //= 2
        m-= 1
        if a[0] < a[1]:
            a[0],a[1] = a[1],a[0]
else:
    while m > 0:
        a[0] //= 2
        m -= 1
        for i in range(n-1):
            if a[0] < a[i]:
                a.insert(0,a.pop(i))
                cnt = i
                break
            elif a[cnt+1] < a[0]:
                break
print(sum(a))