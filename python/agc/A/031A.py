import collections
n = int(input())
s = input()
mod = 10**9+7
ans = 1
s_ = collections.Counter(s)
for i in s_:
    ans *= s_[i] + 1
print((ans-1)%mod)