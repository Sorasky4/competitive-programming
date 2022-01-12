n = int(input())
s = [input() for _ in range(n)]
dic = {}
for i in range(n):
    if s[i] not in dic.keys():
        dic[s[i]] = 1
    else:
        dic[s[i]] += 1
max_v = max(dic.values())
mv_str = []
for k, v in dic.items():
    if v == max_v:
        mv_str.append(k)
ans = sorted(mv_str)
print('\n'.join(map(str,ans)))