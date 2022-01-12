dis1 = list(map(int,input().split()))
dis2 = list(map(int,input().split()))
if dis1[0] in dis2 or dis1[1] in dis2:
    print('YES')
else:
    print('NO')