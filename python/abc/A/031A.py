a,d = map(int,input().split())
aa = (a+1)*d
ad = a*(d+1)
if aa >= ad:
    print(aa)
else:
    print(ad)