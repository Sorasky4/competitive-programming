n = int(input())
a = [int(input()) for i in range(n)]
b = sorted(a,reverse=True)
for i in range(n):
    if b[0] == a[i]:
        ans = b[1]
    else:
        ans = b[0]
    print(ans)