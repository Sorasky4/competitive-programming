a,b,k = map(int,input().split())
ans = []
for i in range(a,a+k):
    if i <= b:
        ans.append(i)
for i in range(b-k+1,b+1):
    if a < i and i not in ans:
        ans.append(i)
for i in range(len(ans)):
    print(ans[i])