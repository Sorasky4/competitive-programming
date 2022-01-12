s = input()
t = input()
for _ in range(len(s)):
    if s == t:
        print('Yes')
        break
    else:
        tmp = s[-1]
        s = tmp + s[:-1]
else:
    print('No')