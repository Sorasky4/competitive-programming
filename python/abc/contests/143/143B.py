n = int(input())
d = [int(i) for i in input().split()]
ans = []
for i in range(n):
    for j in range(n):
        if i < j:
            ans.append(d[i] * d[j])
print(sum(ans))