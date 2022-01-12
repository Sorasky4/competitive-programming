s = input()
t = input()
min_s = sorted(s)
max_t = sorted(t, reverse=True)
if min_s < max_t:
    print('Yes')
else:
    print('No')