n = int(input())
w = list(map(int,input().split()))
v = []
min_ = sum(w)
for i in range(n):
    v.append(w[i])
    w[i] = 0
    min_ = min(abs(sum(v)-sum(w)),min_)
print(min_)