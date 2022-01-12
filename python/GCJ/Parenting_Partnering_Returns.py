# sample2 TLE
T = int(input())
ans = ['IMPOSSIBLE'] * (T+1)
for case in range(T):
    n = int(input())
    tasks = [[int(i) for i in input().split()] for j in range(n)]
    for i in range(2**n):
        ok = True
        C = []
        J = []
        for j in range(n):
            add = [tasks[j][0], tasks[j][1], j]
            if (i >> j) & 1:
                J.append(add)
            else:
                C.append(add)
        if len(C) != 0:
            C.sort(key=lambda x: x[0])
            for j in range(len(C)-1):
                if C[j][1] <= C[j+1][0]:
                    pass
                else:
                    ok = False
        if len(J) != 0:
            J.sort(key=lambda x: x[0])
            for j in range(len(J)-1):
                if J[j][1] <= J[j+1][0]:
                    pass
                else:
                    ok = False
        if ok:
            task = [0]*n
            if len(C) != 0:
                for j in range(len(C)):
                    task[C[j][2]] = 'C'
            if len(J) != 0:
                for j in range(len(J)):
                    task[J[j][2]] = 'J'
            ans[case+1] = task
            break
for i in range(1,T+1):
    print('Case #{}: '.format(i), *ans[i], sep='')