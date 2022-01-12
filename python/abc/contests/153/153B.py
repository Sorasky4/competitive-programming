h, n = map(int,input().split())
a = [int(i) for i in input().split()]

if h <= sum(a):
    print('Yes')
else:
    print('No')