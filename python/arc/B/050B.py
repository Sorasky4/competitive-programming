def f(a):
    R = r - a;B = b - a
    if R < 0 or B < 0:
        return False
    if R//(x-1) + B//(y-1) >= a:
        return True
    return False

r,b = map(int,input().split())
x,y = map(int,input().split())
ok = 0
ng = 10**18 + 1
mid = (ok+ng)//2
while ng - ok != 1:
    if f(mid):
        ok = mid
        mid = (ok+ng)//2
    else:
        ng = mid
        mid = (ok+ng)//2
print(ok)