s = input()
t = ['A', 'B', 'C', 'D', 'E', 'F']
ans = [0] * 6
for i, j in enumerate(t):
    ans[i] += s.count(j)
print(' '.join(map(str,ans)))