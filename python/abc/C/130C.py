w,h,x,y = map(int,input().split())
ans = [w*h/2]
if 2*x == w and 2*y == h:
    ans.append(1)
else:
    ans.append(0)
print(' '.join(map(str,ans)))