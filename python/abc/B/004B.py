c = [[i for i in input().split()] for j in range(4)]
ans = [c[i][::-1] for i in range(3,-1,-1)]
for i in ans:
    print(*i)