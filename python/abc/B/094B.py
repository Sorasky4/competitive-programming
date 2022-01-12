n,m,x = map(int,input().split())
a = [int(i) for i in input().split()]
cnt1 = 0
cnt2 = 0
for i in range(x,n+1):
    if i in a:
        cnt1 += 1
for i in range(x,-1,-1):
    if i in a:
        cnt2 += 1
print(min(cnt1,cnt2))