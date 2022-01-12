n = int(input())
a = [int(i) for i in input().split()]
c = [0] * 8
free = 0
for i in a:
    if i < 400:
        c[0] += 1
    elif i < 800:
        c[1] += 1
    elif i < 1200:
        c[2] += 1
    elif i < 1600:
        c[3] += 1
    elif i < 2000:
        c[4] += 1
    elif i < 2400:
        c[5] += 1
    elif i < 2800:
        c[6] += 1
    elif i < 3200:
        c[7] += 1
    else:
        free += 1
min_ans = len([i for i in c if i > 0])
max_ans = min_ans + free
if min_ans == 0:
    min_ans = 1
print(min_ans, max_ans)