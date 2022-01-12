x = int(input())
'''
if x == 1:
    ans = 1
elif x == 2:
    ans = 2
elif x == 3:
    ans = 2
elif x == 4:
    ans = 3
elif x == 5:
    ans = 3
elif x == 6:
    ans = 3
elif x == 7:
    ans = 4
elif x == 8:
    ans = 4
elif x == 9:
    ans = 4
elif x == 10:
    ans = 4
11から15までは5
122333444455555...の群数列
'''
for i in range(1,x+1):
    if i*(i-1)/2 < x <= i*(i+1)/2:
        ans = i
        break
print(ans)