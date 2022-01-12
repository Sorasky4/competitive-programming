x = int(input())
a = x//11
if x % 11 == 0:
    ans = a*2
elif x % 11 <= 6:
    ans = a*2 + 1
else:
    ans = a*2 + 2
print(ans)