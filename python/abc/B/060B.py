a, b, c = map(int, input().split())
for i in range(0,a*b+1,a):
    if i % b == c:
        print('YES')
        break
else:
    print('NO')