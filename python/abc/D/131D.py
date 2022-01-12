n = int(input())
a = []
b = []
cnt = 0
for _ in range(n):
    a1,b1 = map(int,input().split())
    a.append(a1)
    b.append(b1)
c = sorted(zip(b,a))
for i in range(n):
    cnt += c[i][1]
    if cnt > c[i][0]:
        print('No')
        break
else:
    print('Yes')