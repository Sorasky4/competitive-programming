n = int(input())
l = list(map(int,input().split()))
l.sort(reverse=True)
if 2*l[0] < sum(l):
    print('Yes')
else:
    print('No')