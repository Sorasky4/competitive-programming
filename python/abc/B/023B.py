from collections import deque

n = int(input())
s = input()
if n % 2 == 0:
    print(-1)
else:
    ss = deque('b')
    for i in range(n//2):
        if i % 3 == 0:
            ss.appendleft('a')
            ss.append('c')
        elif i % 3 == 1:
            ss.appendleft('c')
            ss.append('a')
        else:
            ss.appendleft('b')
            ss.append('b')
    if ''.join(map(str,ss)) == s:
        print(n//2)
    else:
        print(-1)