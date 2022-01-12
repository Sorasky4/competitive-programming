def Lucas(n, k):
    if n&k == k:
        return 1
    else:
        return 0

n = int(input())
a = list(map(int, list(input())))
odd = 0
cnt = 0
for i in range(n):
    a[i] -= 1
    if a[i] == 1:
        odd += Lucas(n-1, i)
        cnt = 1
if odd % 2 == 1:
    print(1)
else:
    if cnt == 1:
        print(0)
    else:
        for i in range(n):
            a[i] //= 2
            if a[i] == 1:
                odd += Lucas(n-1, i)
        print(odd%2 * 2)