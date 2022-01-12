'''n = int(input())
l = sorted([int(i) for i in input().split()])
ans = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if l[i]<l[j]+l[k] and l[j]<l[k]+l[i] and l[k]<l[i]+l[j]:
                ans += 1
print(ans)'''

'''n = int(input())
l = sorted([int(i) for i in input().split()])
ans = 0
for i in range(1,n-1):
    for j in range(i-1,-1,-1):
        if l[i+1] - l[i] >= l[j]:
            break
        ans += 1
print(ans)'''

'''import sys
input = sys.stdin.readline
n = int(input())
l = sorted([int(i) for i in input().split()])
ans = 0
for i in range(1,n-1):
    tmp=0
    for j in range(i+1,n):
        if l[j] - l[i] >= l[i-1]:
            break
        else:
            for k in range(tmp,i):
                if l[tmp] > l[j]-l[i]:
                    ans += i-tmp
                    break
                elif l[k] > l[j]-l[i]:
                    tmp = k
                    ans += i-tmp
                    break
print(ans)'''

'''ここまでコンテスト中解法
    ここから解説読んだ解法'''

'''import bisect
n = int(input())
L = sorted([int(i) for i in input().split()])
ans = 0
for b in range(n):
    for a in range(b):
        ab = L[a] + L[b]
        r = bisect.bisect_left(L,ab)
        l = b+1
        ans += max(0,r-l)
print(ans)'''