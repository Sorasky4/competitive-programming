x = [int(input()) for _ in range(2)]
if 1 not in x:
    ans = 1
elif 2 not in x:
    ans = 2
else:
    ans = 3
print(ans)