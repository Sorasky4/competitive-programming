n = int(input())
s = input()
cnt = 1
if n == 1:
    print(cnt)
else:
    for i in range(n-1):
        if s[i] != s[i+1]:
            cnt += 1
    print(cnt)