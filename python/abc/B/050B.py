n = int(input())
t = [int(i) for i in input().split()]
m = int(input())
total = sum(t)
for i in range(m):
    ans = total
    p, x = map(int, input().split())
    ans -= t[p-1] - x
    print(ans)