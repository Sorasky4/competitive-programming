s = input()
color = [0, 0]
for i in s:
    if i == '0':
        color[0] += 1
    else:
        color[1] += 1
print(min(color) * 2)