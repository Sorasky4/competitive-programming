s = input()
t = input()

dic_s = {}
dic_t = {}

for i, j in zip(s, t):
    if i not in dic_s.keys():
        dic_s[i] = 1
    else:
        dic_s[i] += 1
    if j not in dic_t.keys():
        dic_t[j] = 1
    else:
        dic_t[j] += 1

dic_s = sorted(dic_s.items(), key=lambda x: x[1])
dic_t = sorted(dic_t.items(), key=lambda x: x[1])

for i in range(min(len(dic_s), len(dic_t))):
    if dic_s[i][1] != dic_t[i][1]:
        print('No')
        exit()
print('Yes')