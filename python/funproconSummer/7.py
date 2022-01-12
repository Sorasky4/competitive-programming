import collections
n = int(input())
s = [input() for i in range(n)]
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
ans = [0]*len(alpha)
new_s = ''.join(map(str,s))
for i in range(len(alpha)):
    ans[i] = new_s.count(alpha[i])
for i in range(len(alpha)):
    print(alpha[i]+' : '+str(ans[i]))


'''辞書型
for k,v in dict.items():
    print('{} : {}',format(k,v))みたいな書き方'''