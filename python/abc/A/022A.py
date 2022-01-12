n,s,t = map(int,input().split())
w = int(input())
a = [int(input()) for i in range(n-1)]
b = [0]*n
b[0] = w
cnt = 0
for i in range(n-1):
    b[i+1] = b[i] + a[i]
for i in range(n):
    if s <= b[i] and b[i] <= t:
        cnt += 1
print(cnt)