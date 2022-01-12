w,h,n = map(int,input().split())
up = h
down = 0
left = 0
right = w
for i in range(n):
    x, y, a = map(int,input().split())
    if a == 1:
        left = max(left,x)
    elif a == 2:
        right = min(right,x)
    elif a == 3:
        down = max(down,y)
    else:
        up = min(up,y)
print(max(0, right - left) * max(0, up - down))