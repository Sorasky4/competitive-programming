h = int(input())
ans = 0
while h > 0:
    h //= 2
    ans += 1
print(2**ans - 1)