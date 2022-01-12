n = int(input())
for i in range(int(n**(1/2)),0,-1):
    if i ** 2 <= n:
        print(i**2)
        exit()