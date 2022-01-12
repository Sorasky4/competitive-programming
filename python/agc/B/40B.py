import bisect
n = int(input())
l = []
r = []
d = []
dmax = 0
ans = 0
for i in range(n):
    l1,r1 = map(int,input().split())
    l.append(l1)
    r.append(r1)
    d.append(r1-l1 + 1)
    dmax = max(dmax,d[i])
mylist = sorted(zip(l,r,d))
if dmax == mylist[0][2]:
    ans += mylist[0][2] + max(0,min(mylist[1:][1])-mylist[-1][0]+1)
elif dmax == mylist[-1][2]:
    ans += mylist[-1][2] + max(0,min(mylist[:-1][1])-mylist[-2][0]+1)
#print(ans,mylist[0][1:2],mylist[-1][0])
#print(mylist)