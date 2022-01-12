s=list(input())
a=sorted(s)
if a.count(a[0]) == 2 and a.count(a[2]) == 2:
    print('Yes')
else:
    print('No')