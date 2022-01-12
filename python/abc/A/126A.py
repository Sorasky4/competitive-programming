n,k=map(int,input().split())
s=list(input())
s[k-1] = s[k-1].lower()
z = ''
for i in range(n):
    z +=s[i]
print(z)