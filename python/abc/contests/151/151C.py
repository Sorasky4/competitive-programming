n,m = map(int,input().split())
ps = []
for i in range(m):
    ppss = [i for i in input().split()]
    ps.append(ppss)
ac = [0 for i in range(n)]
wa = [0 for i in range(n)]
for i in range(m):
    if ps[i][1] == 'AC':
        ac[int(ps[i][0])-1] = 1
    else:
        if ac[int(ps[i][0])-1] != 1:
            wa[int(ps[i][0])-1] += 1
for i in range(n):
    if ac[i] != 1:
        wa[i] = 0
print(sum(ac),sum(wa))