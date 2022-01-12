k,x=map(int,input().split())
a=[0]*(k*2-1)
for i in range(k*2-1):
    a[i] = x-k+1+i
b = map(str,a)
print(' '.join(b))