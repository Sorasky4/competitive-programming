n,k = map(int,input().split())
m = int(input())
line = [int(i) for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    tmp = line[a-1:b]
    del line[a-1:b]
    line = line + tmp
tech = line.index(k-1) + 1
full = line.index(k) + 1
print(tech)
print(full)