n = int(input())
v = [int(i) for i in input().split()]
odd = [[0,i] for i in range(10**5+1)]
even = [[0,i] for i in range(10**5+1)]
for i in v[0:n-1:2]:
    odd[i][0] += 1
for i in v[1:n:2]:
    even[i][0] += 1
odd.sort(reverse=True)
even.sort(reverse=True)
if odd[0][1] != even[0][1]:
    ans = n//2 - odd[0][0] + n//2 - even[0][0]
else:
    ans=min(n//2-odd[0][0]+n//2-even[1][0],n//2-odd[1][0]+n//2-even[0][0])
print(ans)