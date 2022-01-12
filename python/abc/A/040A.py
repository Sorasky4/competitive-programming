n,x = map(int,input().split())
if x > n/2:
    print(int(n-x))
else:
    print(int(x-1))