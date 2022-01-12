a,b,t=map(int,input().split())
sum=0
i=1
while a*i <= t+0.5:
    sum += b
    i += 1
print(sum)