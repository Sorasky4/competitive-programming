n,m = map(int,input().split())
a = [list(map(int,input().split())) for i in range(n)]
s = set(a[0][1:])
for i in range(1,len(a)):
    s = set(a[i][1:]) & s
print(len(s))