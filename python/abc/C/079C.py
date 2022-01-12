s=input()
for i in range(2**3):
    op = ['+','+','+']
    for j in range(3):
        if ((i >> j) & 1):
            op[j] = '-'
    if eval(s[0]+op[0]+s[1]+op[1]+s[2]+op[2]+s[3]) == 7:
        print(s[0]+op[0]+s[1]+op[1]+s[2]+op[2]+s[3]+'=7')
        break