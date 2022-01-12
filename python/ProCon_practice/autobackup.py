i = int(input())
n = int(input())
sh = int(input())
sm = int(input())
l = int(input())
s = 0
b = []
c = [sh,sm]
b.append(c)
while l > 0:
    s += 1
    sm += 1
    if sm >= 60:
        sm = 0
        sh += 1
    if s % i == 0:
        c = [sh,sm]
        b.insert(0,c)
    l -= 1
c = [sh,sm]
b.insert(0,c)
if n <= len(b):
    print(b[n-1][0])
    print(b[n-1][1])
else:
    print(b[-1][0])
    print(b[-1][1])