s = input()
k = int(input())
ans = []
for i in range(len(s)-k+1):
    ans.append(s[i:i+k])
ans = (set(ans))
print(len(ans))