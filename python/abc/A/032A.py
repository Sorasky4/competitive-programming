a = int(input())
b = int(input())
n = int(input())
L = a*b
i = 2
if a < b:
    a,b = b,a
r = a % b
while r != 0:
    a = b
    b = r
    r = a % b
L /= b
ans = L
while ans < n:
    ans = L*i
    i += 1
print(int(ans))