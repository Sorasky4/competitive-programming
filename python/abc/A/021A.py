n = int(input())
cnt = 1
ans = [0]
if n % 2 != 0:
    ans.append(1)
    n -= 1
while 0 < n:
    ans.append(2)
    cnt += 1
    n -= 2
ans[0] = len(ans) - 1
for i in range(len(ans)):
    print(ans[i])