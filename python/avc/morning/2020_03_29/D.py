n = int(input())
d = [int(input()) for _ in range(n)]
max_ = max(d)
sum_ = sum(d)
print(sum_)
if max_ >= sum_ - max_:
    print(max_ - (sum_ - max_))
else:
    print(0)