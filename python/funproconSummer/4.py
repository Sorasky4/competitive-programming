w = int(input())
d = int(input())
c = int(input())
a = min(w,d)
if a%(c*2) == 0:
    ans = a // (c*2)
else:
    ans = a // (c*2) + 1
print(ans)