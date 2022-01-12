'''s = list(str(input()))
l = int(len(s))
a = list(range(l))
for i in range(l):
    a[i] = 1
a = [int(j) for j in a]
for i in range(l-2):
    if s[i] == s[i+1] == 'R':
        a[i+2] += a[i]
        a[i] = 0
for i in range(l)[::-1]:
    if s[i] == s[i-1] == 'L':
        a[i-2] += a[i]
        a[i] = 0
print(' '.join(map(str,a)))'''

s = list(input())
l = len(s)
a = [1]*l
for i in range(l-2):
    if s[i] == s[i+1] == 'R':
        a[i+2] += a[i]
        a[i] = 0
for i in range(l)[::-1]:
    if s[i] == s[i-1] == 'L':
        a[i-2] += a[i]
        a[i] = 0
print(' '.join(map(str,a)))