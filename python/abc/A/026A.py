a = int(input())
if a % 2 == 0:
    ans = (a/2)**2
else:
    ans = (a-1)/2*((a-1)/2+1)
print(int(ans))