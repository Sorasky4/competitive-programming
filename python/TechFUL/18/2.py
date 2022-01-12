import math

w = int(input())
h = int(input())
d = int(input())
c = math.cos(math.radians(d))
s = math.sin(math.radians(d))
if c < 0:
    c = -c
if s < 0:
    s = -s
w_ = w*c + h*s
h_ = h*c + w*s
print(int(w_))
print(int(h_))