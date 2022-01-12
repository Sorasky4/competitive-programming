'''
n = int(input())
a = [int(i) for i in input().split()]
a = [0] + a
for i in range(n,0,-1):
    a[i] = sum(a[i::i]) % 2
ans = []
for i in range(len(a)):
    if a[i] == 1:
        ans.append(i)
print(len(ans))
if len(ans) != 0:
    print(' '.join(map(str,ans)))
'''
n = int(input())
a = [int(i) for i in input().split()]
for i in range(n-1,0,-1):
    a[i] = sum(a[i::i+1]) % 2
a[0] = sum(a) % 2
ans = []
for i in range(n):
    if a[i] == 1:
        ans.append(i+1)
print(len(ans))
if len(ans) != 0:
    print(' '.join(map(str,ans)))