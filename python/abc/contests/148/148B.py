n = int(input())
x = [i for i in input().split()]
ans = []
for i in range(n):
    ans.append(x[0][i])
    ans.append(x[1][i])
print(''.join(map(str,ans)))