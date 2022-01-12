from itertools import combinations_with_replacement

n, m, q = map(int, input().split())
p = []
ans = 0
for _ in range(q):
    p.append(list(map(int, input().split())))
for A in combinations_with_replacement(range(1,m+1), n):
    cnt = 0
    for i in range(q):
        if A[p[i][1]-1] - A[p[i][0]-1] == p[i][2]:
            cnt += p[i][3]
    ans = max(ans, cnt)
print(ans)