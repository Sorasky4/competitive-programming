n,k,q = map(int,input().split())
a = [int(input()) for i in range(q)]
b = q - k
c = [0]*n
for i in range(len(a)):
    a[i] -= 1
    c[a[i]] += 1
for i in range(n):
    if c[i] > b:
        print('Yes')
    else:
        print('No')