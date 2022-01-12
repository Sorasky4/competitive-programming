n = int(input())
red = []
blue = []
for i in range(n):
    x, c = map(str, input().split())
    if c == 'R':
        red.append(int(x))
    else:
        blue.append(int(x))
if red:
    red.sort()
if blue:
    blue.sort()
for i in range(len(red)):
    print(red[i])
for i in range(len(blue)):
    print(blue[i])