s = sorted(input())
t = sorted(input(), reverse=True)

for i in range(min(len(s), len(t))):
    if ord(s[i]) < ord(t[i]):
        print('Yes')
        exit()
    elif ord(s[i]) > ord(t[i]):
        print('No')
        exit()
if len(s) < len(t):
    print('Yes')
else:
    print('No')