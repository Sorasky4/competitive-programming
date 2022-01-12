n = int(input())
ans = 1000000
for i in range(1,int(n**(1/2))+1):
    dif = abs(i - n//i)
    res = n - i * (n // i)
    ans = min(ans, dif + res)
print(ans)