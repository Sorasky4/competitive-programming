n,k = map(int,input().split())
a = [int(i) for i in input().split()]
m = [int(i) for i in range(n)]
b = list(zip(a,m))
b.sort(reverse=True)
ans = ':('
for i in range(k):
    if b[i][1] == 0:
        ans = 'Yes!'
        break
print(ans)