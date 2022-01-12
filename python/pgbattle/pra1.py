n, k = map(int, input().split())
a = list(map(int, input().split()))
t = 0

for i in a:
    if i > k:
        t += i - k
print(t)