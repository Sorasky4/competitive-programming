l,x,y,s,d = map(int,input().split())
if s <= d:
  ans1 = (d-s)/(x+y)
  if y > x:
    ans2 = (l-(d-s))/(y-x)
  else:
    ans2 = ans1
else:
  ans1 = (l-(s-d))/(x+y)
  if y > x:
    ans2 = (s-d)/(y-x)
  else:
    ans2 = ans1
print(min(ans1,ans2))