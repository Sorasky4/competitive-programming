n = int(input())
a = list(map(int,input().split()))
m = [[0 for i in range(n)]for j in range(n)]
cnt = 0
for i in range(n):
    a[i] -= 1
    m[i][a[i]] = 1