w = int(input())
h = int(input())
if w == 1 and h == 1:
    print(0)
elif w == 1 or h == 1:
    print((w*h-1)*2)
elif (w*h)%2==0:
    print(w*h)
else:
    print(w*h+1)