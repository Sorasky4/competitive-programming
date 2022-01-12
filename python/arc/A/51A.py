x1,y1,r = map(int,input().split())
bl,bf,br,bc = map(int,input().split())
rc = y1 + r
rf = y1 - r
rr = x1 + r
rl = x1 - r
if rc <= bc and bf <= rf and bl <= rl and rr <= br:
    blue = 'YES'
    red = 'NO'
elif ((br-x1)**2+(bc-y1)**2)<=r**2 and ((bl-x1)**2+(bc-y1)**2)<=r**2 and ((bl-x1)**2+(bf-y1)**2)<=r**2 and ((br-x1)**2+(bf-y1)**2)<=r**2:
    blue = 'NO'
    red = 'YES'
else:
    blue = 'YES'
    red = 'YES'
print(red)
print(blue)