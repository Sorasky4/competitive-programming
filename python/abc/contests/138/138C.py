n = int(input())
v = list(map(int,input().split()))
v_ = sorted(v)
ans = (v_[0] +v_[1])/2
for i in range(2,n):
    ans = (ans + v_[i])/2
print(ans)