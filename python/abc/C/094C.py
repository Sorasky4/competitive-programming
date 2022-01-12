n = int(input())
a = [int(i) for i in input().split()]
b = sorted(a)
cl = b[(n-1)//2]
cr = b[n//2]
for i in range(n):
    if a[i] <= cl:
        print(cr)
    elif cr <= a[i]:
        print(cl)