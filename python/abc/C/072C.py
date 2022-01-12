n = int(input())
a = sorted([int(i) for i in input().split()])
ans = 1
dic = {}
for i in range(10**5):
    dic[i] = 0
for i in a:
    dic[i] += 1
for i in range(1,10**5-1):
    ans = max(ans, dic[i-1] + dic[i] + dic[i+1])
print(ans)