s = input()
t = input()
at = ['a','t','c','o','d','e','r']
ok = True
for i in range(len(s)):
    if s[i] == t[i]:
        continue
    elif s[i] == '@':
        if t[i] in at:
            continue
        else:
            ok = False
            break
    elif t[i] == '@':
        if s[i] in at:
            continue
        else:
            ok = False
            break
    else:
        ok = False
        break
if ok:
    print('You can win')
else:
    print('You will lose')