T = int(input())
for case in range(T):
    N = int(input())
    a = [[int(i) for i in input().split()] for j in range(N)]
    k = 0
    r = 0
    c = 0
    for i in range(N):
        k += a[i][i]
        if len(a[i]) != len(set(a[i])):
            r += 1
        s = []
        for j in range(N):
            s.append(a[j][i])
        if len(s) != len(set(s)):
            c += 1
    print('Case #{}:'.format(case+1), k, r, c)