n = int(input())
a = [int(input()) for _ in range(n)]
button = 0
for i in range(n):
    button = a[button] - 1
    ans = i + 1
    if button == 1:
        print(ans)
        break
else:
    print(-1)