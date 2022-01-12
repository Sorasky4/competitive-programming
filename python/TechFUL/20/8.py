'''
n = int(input())
t = [int(i) for i in input().split()]
r = [int(i) for i in input().split()]
a = [[(t[i]+t[i+1])-r[i],int(i)] for i in range(n-1)]
a.sort(reverse=True)
print(a)
ans = 0
for i in range(n-1):
    if a[i][0] > 0 and t[a[i][1]] != 0 and t[a[i][1]+1] != 0:
        ans += r[a[i][1]]
        t[a[i][1]] = t[a[i][1]+1] = 0
ans += sum(t)
print(ans)
貪欲もdpもわからん
'''
n = int(input())
t = [int(i) for i in input().split()]
r = [int(i) for i in input().split()]
ans = 0
tmp = 0
for i in range(n-1):
    if t[i] + t[i+1] > r[i]:
        ans += r[i]
        tmp = t[i]
    elif tmp == 0:
        ans += t[i]
    if i > 0:
        if tmp != 0:
            if tmp + r[i] < r[i-1]:
                ans -= r[i-1]
                ans += tmp
            elif t[i] + t[i+1] > r[i]:
                tmp = 0
                ans -= r[i]
print(ans)
#わからん