n = int(input())
a = [int(i) for i in input().split()]
cnt = 0
total = 0
for i in a:
    if i != 0:
        cnt += 1
        total += i
print(-(-total // cnt))