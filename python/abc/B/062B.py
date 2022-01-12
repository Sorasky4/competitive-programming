h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
for i in range(h):
    a[i].insert(0,'#')
    a[i].append('#')
wall = ['#' for _ in range(w+2)]
a.insert(0, wall)
a.append(wall)
for i in a:
    print(*i, sep='')