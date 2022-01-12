x = [int(i) for i in input().split()]
n = x[0]
a = x[1]
b = x[2]
if (b - a) % 2 == 0:
    ans = b - (a + b) // 2
else:
    if a - 1 <= n - b:
        tmp = b - a
        ans = tmp - (1 + tmp) // 2 + a
        if b - 1 <= a:
            ans = b - 1
    else:
        tmp = a + n - b + 1
        ans = n - (n + tmp) // 2 + (n - b + 1)
        if n - a <= n - b + 1:
            ans = n - a
print(ans)