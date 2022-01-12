t = int(input())
for _ in range(t):
    a,b,n,s=map(int,input().split())
    if s <= b:
        print('YES')
        continue
    else:
        if s < n:
            print('NO')
        elif s//n <= a:
            if s%n <= b:
                print('YES')
            else:
                print('NO')
        else:
            if (s-a*n) <= b:
                print('YES')
            else:
                print('NO')