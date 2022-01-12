n = int(input())
for i in range(n,1000):
    if str(i)[0] == str(i)[1] == str(i)[-1]:
        ans = i
        break
print(ans)