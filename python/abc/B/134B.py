n,d=map(int,input().split())
o = int(n / (d*2+1))
if n % (d*2+1) == 0:
    print(o)
else:
    print(o+1)