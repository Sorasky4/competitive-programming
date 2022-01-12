t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    cnt = n-1
    for i in range(1,n):
#        if i != 1:
#            if a.index(i) - (i-1) > cnt:
#                continue
        flag = 1
        now = a.index(i)
        while cnt and flag:
            flag = 0
            if now != 0:
                if a[now] < a[now-1]:
                    a[now],a[now-1] = a[now-1],a[now]
                    now -= 1
                    cnt -= 1
                    flag = 1
    print(' '.join(map(str,a)))