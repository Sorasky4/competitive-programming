c = input()
y = input()
n = int(input())
ans = 0
i = 0
while n > 0:
    for j in range(len(c)):
        if y[i] == c[j]:
            i += 1
            n -= 1
            if i == len(y):
                i = 0
            if n == 0:
                break
    else:
        ans += 1
print(ans)