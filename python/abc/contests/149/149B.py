x = [int(i) for i in input().split()]
ans1 = x[0]
ans2 = x[1]
if ans1 >= x[2]:
    ans1 -= x[2]
else:
    x[2] -= ans1
    ans1 = 0
    ans2 = max(0,ans2 - x[2])
print(ans1,ans2)