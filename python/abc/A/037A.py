a,b,c = map(int,input().split())
cnt = 0
while c > 0:
    c -= min(a,b)
    cnt += 1
    if c < 0:
        cnt -= 1
print(cnt)