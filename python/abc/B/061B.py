n, m = map(int, input().split())
dic = {}
for i in range(1,n+1):
    dic[i] = 0
for i in range(m):
    a, b = map(int, input().split())
    dic[a] += 1
    dic[b] += 1
for i in range(1,n+1):
    print(dic[i])