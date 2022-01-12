a = [int(input()) for i in range(3)]
b = sorted(a,reverse=True)
for i in range(3):
    for j in range(3):
        if a[i] == b[j]:
            print(j+1)