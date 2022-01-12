n = int(input())
w = list(map(str, input().split()))
w[-1] = w[-1][:-1]
k = ['TAKAHASHIKUN', 'Takahashikun', 'takahashikun']
ans = 0


for i in w:
    if i in k:
        ans += 1


print(ans)