a,b = map(int,input().split())
if abs(a-b) % 2 == 0:
    print(min(a,b)+(abs(a-b)//2))
else:
    print('IMPOSSIBLE')