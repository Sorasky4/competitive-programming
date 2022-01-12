n = [input() for i in range(5)]
flag = 1
ans = 0
l = []
while flag:
    flag = 0
    for i in range(len(n)-1,0,-1):
        if n[i][-1] < n[i-1][-1]:
            n[i],n[i-1] = n[i-1],n[i]
            flag = 1
for i in range(len(n)):
    if n[i][-1] != '0':
        n[i] = int(n[i])
        l = n.pop(i)
        break
for i in range(len(n)):
    n[i] = int(n[i])
for i in range(len(n)):
    while n[i]%10 != 0:
        n[i] += 1
    ans += n[i]
if l:
    ans += l
print(ans)