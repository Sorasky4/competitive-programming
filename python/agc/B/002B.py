'''
n,m = map(int,input().split())
z = []
box = [0] + [1 for _ in range(n)]
ans = 1
red1 = True
for i in range(m):
    x,y=map(str,input().split())
    box[int(x)] -= 1
    box[int(y)] += 1
    if red1 == False and x in z:
        z += y
    if x == '1' and red1:
        red1 = False
        z += y
    if box[int(x)] == 0 and x in z:
        z.remove(x)
ans = max(ans,len(set(z)))
print(ans)
'''

n,m = map(int,input().split())
box = [0] + [1 for _ in range(n)]
red = [0] + [1] + [0 for _ in range(n-1)]
for i in range(m):
    x,y=map(int,input().split())
    if red[x] == 1:
        red[y] = 1
    box[x] -= 1
    box[y] += 1
    if box[x] == 0:
        red[x] = 0
print(sum(red))