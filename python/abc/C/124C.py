s = input()
lb = 0
lw = 0
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == '0':
            lb += 1
        else:
            lw += 1
    else:
        if s[i] == '0':
            lw += 1
        else:
            lb += 1
print(min(lb,lw))