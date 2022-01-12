'''
a,b,x = map(int,input().split())
m = 10**9
if a*m + b*10 <= x:
    print(m)
    exit(0)
else:
    for i in range(8,-1,-1):
        if a*(10**i) + b*(i+1) <= x:
            d = i+1
            break
    else:
        print(0)
        exit(0)
    x -= b*d
    ans = x//a
    if ans >= 10**d:
        ans = 10**d - 1
    print(ans)
'''

a,b,x = map(int,input().split())
byr = 10**9+1
byl = 0
mid = (byl+byr)//2
while byr - byl > 1:
    if a*mid+b*len(str(mid)) <= x:
        byl = mid
        mid = (byl+byr)//2
    else:
        byr = mid
        mid = (byl+byr)//2
print(byl)