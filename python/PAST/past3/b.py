N, M, Q = map(int, input().split())
person = [[] for _ in range(N)]
solved = [0]*M
for _ in range(Q):
    s = list(map(lambda x: int(x)-1, input().split()))
    if s[0] == 1:
        person[s[1]].append(s[2])
        solved[s[2]] += 1
    else:
        ans = 0
        for i in person[s[1]]:
            ans += (N - solved[i])
        print(ans)