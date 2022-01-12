import math
n, k = map(int,input().split())
ans = math.floor(math.log(n, k)) + 1
print(ans)