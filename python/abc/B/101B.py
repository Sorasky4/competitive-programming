'''n = input()
l = len(n)
n = int(n)
b = n
a = [0]*l
for i in range(l-1,-1,-1):
    a[i] = n // 10**i
    n = n - a[i]*10**i
s = sum(a)
if b % s == 0:
    print('Yes')
else:
    print('No')'''
n = input()
s = [int(i) for i in n]
if int(n) % sum(s) == 0:
    print('Yes')
else:
    print('No')