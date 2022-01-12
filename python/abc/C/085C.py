n,Y = map(int,input().split())
for i in range(Y//10000 + 1):
    x = i
    for j in range((Y-10000*x)//5000 + 1):
        y = j
        z = n - x - y
        if x*10000 + y*5000 + z*1000 == Y:
                print(x,y,z)
                exit(0)
else:
    print('-1 -1 -1')