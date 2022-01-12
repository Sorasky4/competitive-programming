birth = list(map(int,input().split()))
today = list(map(int,input().split()))
if birth[0] < today[0]:
    ans = today[0] - birth[0] + 1
else:
    ans = 1
print(ans)