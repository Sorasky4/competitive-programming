p = int(input())
a = p // 10000
if p - a*10000 >= 5000:
    b = 1
else:
    b = 0
c = (p - a*10000 - b*5000) // 1000
if p - a*10000 - b*5000 - c*1000 >= 500:
    d = 1
else:
    d = 0
e = (p - a*10000 - b*5000 - c*1000 - d*500) // 100
if p - a*10000 - b*5000 - c*1000 - d*500 - e*100 >= 50:
    f = 1
else:
    f = 0
g = (p - a*10000 - b*5000 - c*1000 - d*500 - e*100 - f*50) // 10
if p - a*10000 - b*5000 - c*1000 - d*500 - e*100 - f*50 - g*10 >= 5:
    h = 1
else:
    h = 0
i = p - a*10000 - b*5000 - c*1000 - d*500 - e*100 - f*50 - g*10 - h*5
if a != 0:
    print('10000円は'+str(a)+'枚')
if b != 0:
    print('5000円は'+str(b)+'枚')
if c != 0:
    print('1000円は'+str(c)+'枚')
if d != 0:
    print('500円は'+str(d)+'枚')
if e != 0:
    print('100円は'+str(e)+'枚')
if f != 0:
    print('50円は'+str(f)+'枚')
if g != 0:
    print('10円は'+str(g)+'枚')
if h != 0:
    print('5円は'+str(h)+'枚')
if i != 0:
    print('1円は'+str(i)+'枚')