h, w, k = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = 0
for i in range(2 ** (h-1)):
    