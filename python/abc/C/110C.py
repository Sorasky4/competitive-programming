s = input()
t = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
dic_s = {}
dic_t = {}
for i in alpha:
    dic_s[i] = 0
    dic_t[i] = 0
for i, j in zip(s, t):
    dic_s[i] += 1
    dic_t[j] += 1
val_s = sorted(dic_s.values())
val_t = sorted(dic_t.values())
ans = 'Yes'
for i, j in zip(val_s, val_t):
    if i != j:
        ans = 'No'
        break
print(ans)