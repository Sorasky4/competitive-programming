s = input()
Ccnt = 0
cnt = 0
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = s[2:-1]
for i in range(len(b)):
    if b[i] == 'C':
        Ccnt += 1
for i in range(len(s)):
    if s[i] in a:
        cnt += 1
if s[0] == 'A' and Ccnt == 1 and cnt == 2:
    print('AC')
else:
    print('WA')