t = int(input())
for _ in range(t):
    s = input()
    ans = 0
    cnt = 0
    for i in s:
        if i == 'R':
            cnt = 0
            continue
        else:
            cnt += 1
        ans = max(ans, cnt)
    print(ans+1)