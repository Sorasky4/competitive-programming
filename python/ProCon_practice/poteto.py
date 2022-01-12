def cmb(n,r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
    
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
    
    return result
import random
import time
n = int(input())
#a = list(map(str,input().split()))
a = [str(random.randint(1,100000000)) for i in range(n)]
tik = time.time()
b = []
#k = 2
even_cmb = 0
odd_cmb = 0
for i in range(n):
    b.append(int(a[i][-1]))
even_cnt = 0
for i in range(n):
    if b[i]%2 == 0:
        even_cnt += 1
odd_cnt = n - even_cnt
#print('奇数の数:'+str(odd_cnt)+' '+'偶数の数:'+str(even_cnt))
'''for i in range(even_cnt):
    even_cmb += cmb(even_cnt,i)'''
even_cmb += 2**even_cnt - 1
'''while k <= odd_cnt:
    odd_cmb += cmb(odd_cnt,k)
    k += 2'''
if odd_cnt != 0:
    odd_cmb += 2**(odd_cnt-1) - 1
#print('偶数コンビネーション:'+str(even_cmb))
print('奇数コンビネーション:'+str(odd_cmb))
if even_cmb == 0 and odd_cmb == 1:
    ans = 1
else:
    ans = even_cmb + odd_cmb + even_cmb*odd_cmb
tok = time.time() - tik
print(ans)
print('実行時間:'+str(tok))