a,b = map(int,input().split())
if a == b:
    print(a+b)
else:
    first = max(a,b)
    second = max(a,b)-1
    print(first+second)