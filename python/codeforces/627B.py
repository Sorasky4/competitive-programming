# ハックされたコード
'''
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 'NO'
    for i in range(n-2):
        if a[i] == a[i+1] == a[i+2]:
            ans = 'YES'
            break
    else:
        b = [0] * (n + 1)
        for i in range(1,n):
            if i == 1:
                if a[i-1] != a[i]:
                    b[a[i-1]] += 1
                    b[a[i]] += 1
            else:
                if a[i-1] != a[i]:
                    b[a[i]] += 1
        for i in b:
            if i > 1:
                ans = 'YES'
                break
    print(ans)
'''

# 修正
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 'NO'
    for i in range(n-2):
        if a[i] == a[i+1] == a[i+2]:
            ans = 'YES'
            break
    else:
        b = [0] * (n + 1)
        b[a[0]] += 1
        for i in range(1,n):
            if a[i-1] != a[i]:
                b[a[i]] += 1
        for i in b:
            if i > 1:
                ans = 'YES'
                break
    print(ans)