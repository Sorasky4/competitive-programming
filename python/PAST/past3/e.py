n, m, q = map(int, input().split())
gra = [[0] for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x: int(x)-1, input().split())
    gra[u].append(v)
    gra[v].append(u)
c = [int(i) for i in input().split()]
for i, v in enumerate(c):
    gra[i][0] = v

for _ in range(q):
    s = list(map(lambda x: int(x)-1, input().split()))
    color = gra[s[1]][0]
    print(color)
    if s[0] == 0:
        for i in range(len(gra[s[1]])):
            if i == 0:
                continue
            gra[gra[s[1]][i]][0] = color
    else:
        gra[s[1]][0] = s[2] + 1