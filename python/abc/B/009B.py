n = int(input())
a = sorted([int(input()) for _ in range(n)], reverse=True)
for i in a:
    if i != max(a):
        print(i)
        exit()