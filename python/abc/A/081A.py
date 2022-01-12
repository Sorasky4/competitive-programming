s=str(input())
a=0
if s[0]=="1":
    a+=1
if s[1]=="1":
    a+=1
if s[-1:]=="1":
    a+=1
print(a)