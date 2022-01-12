def function(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())
a = [s]
i = 1
while len(set(a)) == len(a):
    a.append(function(a[i-1]))
    i += 1
print(len(a))