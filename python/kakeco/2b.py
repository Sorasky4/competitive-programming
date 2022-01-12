a = [int(i) for i in input().split()]
if sum(a) % 4 == 0:
    print('Yes')
else:
    print('No')