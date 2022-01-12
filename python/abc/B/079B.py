n = int(input())
l0,l1 = 2,1
if n == 1:
    ans = l1
elif n == 2:
    ans = l0 + l1
else:
    for i in range(1,n):
        ans = l0 + l1
        l0 = ans
        l0,l1 = l1,l0
print(ans)