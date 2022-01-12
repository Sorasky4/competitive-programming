s = str(input())
num26 = 'abcdefghijklmnopqrstuvwxyz'
ans = 0
if s.isalpha():
    if len(s) == 1:
        for i in range(len(num26)):
            if s == num26[i]:
                ans = i
    elif len(s) == 2:
        for i in range(len(num26)):
            if s[0] == num26[i]:
                ans += 26*i
            if s[1] == num26[i]:
                ans += i
    elif len(s) == 3:
        for i in range(len(num26)):
            if s[0] == num26[i]:
                ans += 26**2*i
            if s[1] == num26[i]:
                ans += 26*i
            if s[2] == num26[i]:
                ans += i
    elif len(s) == 4:
        for i in range(len(num26)):
            if s[0] == num26[i]:
                ans += 26**3*i
            if s[1] == num26[i]:
                ans += 26**2*i
            if s[2] == num26[i]:
                ans += 26*i
            if s[3] == num26[i]:
                ans += i
    else:
        for i in range(len(num26)):
            if s[0] == num26[i]:
                ans += 26**4*i
            if s[1] == num26[i]:
                ans += 26**3*i
            if s[2] == num26[i]:
                ans += 26**2*i
            if s[3] == num26[i]:
                ans += 26*i
            if s[4] == num26[i]:
                ans += i
else:
    num10 = int(s)
    if num10 <= 25:
        ans = num26[num10%26]
    elif num10 < 26**2:
        ans = num26[num10//26] + num26[num10%26]
    elif num10 < 26**3:
        ans = num26[num10//26**2] + num26[num10//26%26] + num26[num10%26]
    else:
        ans = num26[num10//26**3] + num26[num10//26**2%26] +num26[num10//26%26] + num26[num10%26]
print(ans)