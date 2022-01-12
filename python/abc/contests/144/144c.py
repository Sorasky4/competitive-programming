n = int(input())
a = []
for i in range(1,int(n**0.5)+1):
    if n % i == 0:
        a.append(i+(n/i)-2)
ans = int(min(a))
print(ans)