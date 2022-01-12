n=int(input())
s = list(str(n))
if n % 3 == 0 or '3' in s:
    print('YES')
else:
    print('NO')