c = input()
a = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(a)):
    if a[i] == c:
        print(a[i+1])