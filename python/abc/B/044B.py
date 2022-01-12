w = input()
dic = {}
for i in w:
    if i not in dic.keys():
        dic[i] = 1
    else:
        dic[i] += 1
for i in dic.values():
    if i % 2 != 0:
        print('No')
        exit()
print('Yes')