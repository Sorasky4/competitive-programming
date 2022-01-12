s = str(input())
num26 = 'abcdefghijklmnopqrstuvwxyz'
ans = 0
if s.isalpha():
    for j in range(len(s)):
        for i in range(len(num26)):
            if s[j] == num26[i]:
                ans += i*26**(len(s)-1-j)
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