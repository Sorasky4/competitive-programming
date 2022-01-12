n = int(input())
if 1 <= n <= 81:
    for i in range(1,10):
        for j in range(1,10):
            if n == i*j:
                print('Yes')
                exit()
    else:
        print('No')
else:
    print('No')