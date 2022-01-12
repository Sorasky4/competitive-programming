n, m = map(int, input().split())
stu = []
check = []
for i in range(n):
    stu.append(list(map(int, input().split())))
for i in range(m):
    check.append(list(map(int, input().split())))
for i in stu:
    min_dis = 4 * 10 ** 8 + 1
    for j, k in enumerate(check):
        dis = abs(i[0] - k[0]) + abs(i[1] - k[1])
        if dis < min_dis:
            ans = j + 1
            min_dis = dis
    print(ans)