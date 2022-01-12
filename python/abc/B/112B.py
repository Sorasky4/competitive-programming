N,T = map(int,input().split())
c = []
t = []
for i in range(N):
    c1,t1 = [int(i) for i in input().split()]
    c.append(c1)
    t.append(t1)
ans = 10000
for i in range(N):
  if t[i] <= T:
    ans = min(ans,c[i])
if ans == 10000:
  print('TLE')
else:
  print(ans)