n = int(input())
ans = [[] for i in range(n)]
for i in range(n):
    ss,pp = map(str,input().split())
    ans[i].append(ss)
    ans[i].append(int(pp))
    ans[i].append(i+1)
ans.sort(key=lambda x: (x[0],-x[1]))
for i in range(n):
    print(ans[i][2])