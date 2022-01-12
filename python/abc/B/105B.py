n = int(input())
i = 0
j = 0
ans = 'No'
while i*4 <= n:
    while j*7 <= n:
        if i*4 + j*7 == n:
            ans = 'Yes'
        j += 1
    i += 1
    j = 0
print(ans)