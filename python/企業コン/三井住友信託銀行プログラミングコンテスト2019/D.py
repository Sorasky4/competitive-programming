n = int(input())
s = input()
ans = 0
for i in range(10):
    if str(i) in s:
        tmp1 = s[s.index(str(i))+1:]
        for j in range(10):
            if str(j) in tmp1:
                tmp2 = tmp1[tmp1.index(str(j))+1:]
                for k in range(10):
                    if str(k) in tmp2:
                        ans += 1
print(ans)