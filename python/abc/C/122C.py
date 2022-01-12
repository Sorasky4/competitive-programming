import bisect

n,q = map(int,input().split())
s = input()
l=[]
r=[]
a = []
c = []
for i in range(q):
    l1,r1 = map(int,input().split())
    l.append(l1)
    r.append(r1)
for i in range(n-1):
    if s[i] + s[i+1] == 'AC':
        a.append(i+1)
        c.append(i+2)
for i in range(q):
    ans = 0
    ans = bisect.bisect_right(c,r[i]) - bisect.bisect_left(a,l[i])
    print(ans)