n, z, w = map(int, input().split())
a = list(map(int, input().split()))
if n == 1:
    print(abs(a[0]-w))
    exit()
print(max(abs(a[-1]-w),abs(a[-2]-a[-1])))