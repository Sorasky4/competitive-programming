t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 'NO'
    if all(i % 2 == 0 for i in a) or all(i % 2 != 0 for i in a):
        ans = 'YES'
    print(ans)