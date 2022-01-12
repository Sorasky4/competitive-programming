import bisect
import collections
n,k = map(int,input().split())
a = sorted(list(map(int,input().split())))
ans = []
while a.count(3) <= k:
    if 0 <= bisect.bisect_left(a,3)-1 < len(a) and 0 <= bisect.bisect_right(a,3) < len(a):
        if abs(a[bisect.bisect_left(a,3)-1]-3) <= abs(a[bisect.bisect_right(a,3)]-3):
            ans.append(a[bisect.bisect_left(a,3)-1])
            a[bisect.bisect_left(a,3)-1] = 3
        else:
            ans.append(a[bisect.bisect_right(a,3)])
            a[bisect.bisect_right(a,3)] = 3
    elif 0 <= bisect.bisect_left(a,3)-1 < len(a):
        ans.append(a[bisect.bisect_left(a,3)-1])
        a[bisect.bisect_left(a,3)-1] = 3
    else:
        ans.append(a[bisect.bisect_right(a,3)])
        a[bisect.bisect_right(a,3)] = 3
if ans:
    ans.sort()
    print(' '.join(map(str,ans)))