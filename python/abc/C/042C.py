n, k = map(int, input().split())
d = list(map(str, input().split()))
possible = [str(i) for i in range(10) if str(i) not in d]
for i in range(n,10**5):
    for j in str(i):
        if j not in possible:
            break
    else:
        print(i)
        exit()