n = int(input())
s = [input() for i in range(n)]
cnt = [0]*52
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
for i in range(n):
    for j in range(len(s[i])):
        for k in range(len(alpha)):
            if s[i][j] == alpha[k]:
                cnt[k] += 1
                break
for i in range(52):
    print(alpha[i]+' : '+str(cnt[i]))