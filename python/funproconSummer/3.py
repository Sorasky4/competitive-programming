cx = []
cy = []
r = []
for i in range(2):
    cx1,cy1,r1 = [int(i) for i in input().split()]
    cx.append(cx1)
    cy.append(cy1)
    r.append(r1)
if cx[0] < -256 or 256 <= cx[0] or cx[1] < -256 or 256 <= cx[1] or cy[0] < -256 or 256 <= cy[0] or cy[1] < -256 or 256 <= cy[1] or r[0] < 1 or 51 <= r[0] or r[1] < 1 or 51 <= r[1]:
    print('Error')
else:
    d = (cx[0] - cx[1])**2 + (cy[0] - cy[1])**2
    if (r[0] + r[1])**2 > d:
        print('hit')
    else:
        print('not')