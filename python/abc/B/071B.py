s = sorted(list(set(input())))
alpha = list('abcdefghijklmnopqrstuvwxyz')
for i in alpha:
    if i not in s:
        print(i)
        break
else:
    print('None')