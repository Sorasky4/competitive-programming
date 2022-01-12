n = int(input())
a = list(map(int,input().split()))
b = a[0]
count = 0
for i in range(n):
    if b < a[i]:
        b = a[i]
    if b-2 >= a[i]:
        count = 1
if count == 0:
    print('Yes')
else:
    print('No')