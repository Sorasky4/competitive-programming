k=int(input())
if k%2==0:
    print(int((k/2)**2))
else:
    print(int((k-(k+1)/2)*((k+1)/2)))