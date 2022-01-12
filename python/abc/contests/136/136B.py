n=int(input())
count = 0
i = 1
while i <= n:
    if i < 10:
        count+=1
    elif 10**2 <= i and i < 10**3:
        count+=1
    elif 10**4 <= i and i < 10**5:
        count+=1
    i = i+1
print(count)