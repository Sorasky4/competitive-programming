'''
import math

a, b = map(int, input().split())

for i in range(b+1,1010):
    if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:
        ans = i
        break
else:
    ans = -1
print(ans)
'''


a, b = map(int,input().split())
if b * 10 <= (a * 25 + 24) // 2 and -(-a * 25 // 2) < (b + 1) * 10:
    print(max(-(-a*25//2), b * 10))
else:
    print(-1)