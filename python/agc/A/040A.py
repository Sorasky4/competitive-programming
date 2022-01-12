s = input()
tmp1 = 1
tmp2 = 1
yet = 0
ans = 0
for i in range(len(s)-1):
    if s[i] == '<' and s[i+1] == '<':
        tmp1 += 1
    elif s[i] == '>' and s[i+1] == '>':
        tmp2 += 1
    elif s[i] == '>' and s[i+1] == '<':
        if tmp1 >= tmp2:
            ans += (tmp1*(tmp1+1))//2 + ((tmp2-1)*tmp2)//2
        else:
            ans += (tmp2*(tmp2+1))//2 + ((tmp1-1)*tmp1)//2
        tmp1 = 1
        tmp2 = 1
        yet = i + 1
        if i+1 == len(s)-1:
            ans += 1
if yet != len(s)-1:
    if s[-1] == '>':
        if tmp1 >= tmp2:
            ans += (tmp1*(tmp1+1))//2 + ((tmp2-1)*tmp2)//2
        else:
            ans += (tmp2*(tmp2+1))//2 + ((tmp1-1)*tmp1)//2
    else:
        ans += (tmp1*(tmp1+1))//2
if len(s) == 1:
    ans = 1
print(ans)