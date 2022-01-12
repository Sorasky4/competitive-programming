a,b = map(int,input().split())
c = a
cnt = 1
while b > a:
    a += c
    cnt += 1
print(cnt)