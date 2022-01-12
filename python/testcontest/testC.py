from itertools import permutations
a = list(map(int, input().split()))
n = sum(a)
per = [i for i in range(n)]
ans = 0
for num in permutations(per, n):
    flag = False
    A = []
    B = []
    C = []
    p = 0
    for i in range(3):
        for j in range(a[i]):
            if i == 0:
                A.append(num[p])
            if i == 1:
                B.append(num[p])
            if i == 2:
                C.append(num[p])
            p += 1
    if not (A[0] < B[0] < C[0]):
        continue
    for i in range(3):
        for j in range(a[i]-1):
            if i == 0:
                if A[j] > A[j+1]:
                    flag = True
            if i == 1:
                if B[j] > B[j+1]:
                    flag = True
            if i == 2:
                if C[j] > C[j+1]:
                    flag = True
    if flag:
        continue
    if len(B) == 1:
        pass
    elif len(B) == 2:
        if A[1] > B[1]:
            continue
        if len(C) == 2:
            if B[1] > C[1]:
                continue
    else:
        if A[1] > B[1]:
            continue
        if A[2] > B[2]:
            continue
        if len(C) >= 2:
            if B[1] > C[1]:
                continue
        if len(C) == 3:
            if B[2] > C[2]:
                continue
    ans += 1
print(ans)