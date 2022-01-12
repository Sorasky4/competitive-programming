'''
# 解説AC
from queue import Queue
k = int(input())
q = Queue()
for i in range(1,10):
    q.put(i)
for i in range(k):
    x = q.get()
    if x % 10 != 0:
        q.put(x*10+x%10-1)
    q.put(x*10+x%10)
    if x % 10 != 9:
        q.put(x*10+x%10+1)
print(x)
'''
import sys
k = int(input())
old = [1,2,3,4,5,6,7,8,9]
new = []
count = 9
if k <= count:
    print(old[k-1])
    sys.exit()
else:
    while count < k:
        if len(old) > 0:
            i = old.pop(0)
            last = i%10
            if last != 0:
                new.append(i*10 + (last-1))
                count += 1
                if count == k:
                    break
            new.append(i*10 + last)
            count += 1
            if count == k:
                break
            if last != 9:
                new.append(i*10 + (last+1))
                count += 1
                if count == k:
                    break
        else:
            old = new
            new = []
    print(new[-1])
