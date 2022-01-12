x, y, a, b, c = map(int, input().split())
p = sorted([int(i) for i in input().split()], reverse=True)
q = sorted([int(i) for i in input().split()], reverse=True)
r = sorted([int(i) for i in input().split()], reverse=True)
p = p[:x]
q = q[:y]
apple = sorted(p + q + r, reverse=True)
print(sum(apple[:x+y]))