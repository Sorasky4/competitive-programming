n = int(input())
a, b = map(int, input().split())
k = int(input())
p = [int(i) for i in input().split()]
pl = len(set(p))
if a in p or b in p or k != pl:
    print('NO')
else:
    print('YES')