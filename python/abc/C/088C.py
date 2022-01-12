c = [[int(i) for i in input().split()] for _ in range(3)]
b = [0 for _ in range(3)]
ans = 'Yes'
for i in range(3):
    if i == 0:
        for j in range(3):
            b[j] = c[i][j] - c[i][(j+1)%3]
    else:
        for j in range(3):
            if b[j] != c[i][j] - c[i][(j+1)%3]:
                ans = 'No'
                break
        if ans == 'No':
            break
print(ans)