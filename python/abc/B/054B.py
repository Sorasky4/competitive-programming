n,m = map(int,input().split())
a = [input() for _ in range(n)]
b = [input() for i in range(m)]
ans = 'No'
for i in range(n-m+1):
    for j in range(n-m+1):
        if a[i][j:j+m] == b[0]:
            for k in range(i+1,i+m):
                if a[k][j:j+m] != b[k-i]:
                    break
            else:
                ans = 'Yes'
print(ans)