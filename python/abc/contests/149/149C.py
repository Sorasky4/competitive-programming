def is_prime(n):
    if n == 1: return False
    for k in range(2, int(n**(0.5)) + 1):
        if n % k == 0:
            return False
    return True

x = int(input())
for i in range(x,10**6):
    if is_prime(i):
        ans = i
        break
print(ans)