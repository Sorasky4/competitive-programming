x = int(input())
ans = 1
if x < 4:
    print(1)
else:
    for i in range(2,int(x**(1/2)+1)):
        j = 2
        a = -1
        while a <= x:
            ans = max(ans,a)
            a = i**j
            j += 1
    print(ans)