import math
a,b,x = map(int,input().split())
deep = x/a**2
if deep >= b/2:
    tan = (b-deep)/(a/2)
    ans = (math.atan(tan))*180/math.pi
else:
    tan = b/((2*x)/(a*b))
    ans = (math.atan(tan))*180/math.pi
print(ans)