# 文字列の再構成を繰り返すので比較的遅い
s = input()[::-1]
ans = 'YES'
while s:
    if s[:5] == 'maerd' or s[0:5] == 'esare':
        s = s[5:]
    elif s[:6] == 'resare':
        s = s[6:]
    elif s[:7] == 'remaerd':
        s = s[7:]
    else:
        ans = 'NO'
        break
print(ans)


# 文字列を見るだけなので比較的速い
'''
s = input()[::-1]
n = len(s)
i = 0
ans = 'YES'
while i < n:
    if s[i] == 'm':
        if n - i < 5:
            ans = 'NO'
            break
        if s[i:i+5] == 'maerd':
            i += 5
            continue
        else:
            ans = 'NO'
            break
    elif s[i] == 'e':
        if n - i < 5:
            ans = 'NO'
            break
        if s[i:i+5] == 'esare':
            i += 5
            continue
        else:
            ans = 'NO'
            break
    elif s[i] == 'r':
        if n - i < 6:
            ans = 'NO'
            break
        if s[i:i+6] == 'resare':
            i += 6
            continue
        else:
            if n - i < 7:
                ans = 'NO'
                break
            if s[i:i+7] == 'remaerd':
                i += 7
                continue
            else:
                ans = 'NO'
                break
    else:
        ans = 'NO'
        break
print(ans)
'''