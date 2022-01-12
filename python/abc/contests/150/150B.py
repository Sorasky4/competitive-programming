x = [input() for _ in range(2)]
ans = 0
for i in range(len(x[1])-2):
    if x[1][i] == 'A' and x[1][i+1] == 'B' and x[1][i+2] == 'C':
        ans += 1
print(ans)