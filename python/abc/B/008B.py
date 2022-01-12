n = int(input())
s = [input() for _ in range(n)]
dic = {}
for i in range(n):
    if s[i] not in dic.keys():
        dic[s[i]] = 1
    else:
        dic[s[i]] += 1
max_count = max(dic.values())
for k, v in dic.items():
    if v == max_count:
        print(k)
        exit()