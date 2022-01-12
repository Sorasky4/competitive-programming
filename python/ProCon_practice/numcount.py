s=str(input())
a=[0,1,2,3,4,5,6,7,8,9]
num = 0
for i in range(len(a)):
    a[i] = s.count(str(i))
    if a[i] == 0:
        num += 1
if num == 10:
    print('入力値エラーです。')
else:
    for i in range(len(a)):
        print(str(i) + '=' + str(a[i]) + '個')