a,b = map(int,input().split())
s = str(b)
for i in range(a-1):
    s += str(b)
ss = str(a)
for i in range(b-1):
    ss += str(a)
if s <= ss:
    print(s)
else:
    print(ss)