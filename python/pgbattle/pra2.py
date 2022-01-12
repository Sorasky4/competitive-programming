n, m = map(int, input().split())
a, b, c = map(int, input().split())

for i in range(n+1):
    legtotal = m - c*i
    cretotal = n - i
    '''
    x + y = cretotal
    ax + by = legtotal
    x = cretotal - y
    a(cretotal - y) + by = legtotal
    a*cretotal + (b-a)*y = legtotal
    y = (legtotal - a*cretotal)/(b-a)
    '''
    if b != a:
        y = int((legtotal - a*cretotal)/(b-a))
        x = cretotal - y
        if a*x+b*y == legtotal and x >= 0 and y >= 0:
            z = i
            print(x, y, z)
            exit()
    else:
        if cretotal*a == legtotal:
            x = cretotal
            y = 0
            z = i
            print(x, y, z)
            exit()
print(-1, -1, -1)