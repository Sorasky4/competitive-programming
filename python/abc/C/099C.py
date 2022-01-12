n = int(input())
list6 = [6**i for i in range(7)]
list9 = [9**i for i in range(6)]
m = {}
def ans(n):
    if n <= 5:
        return n
    elif n in m:
        return m[n]
    else:
        m6 = max(i for i in list6 if i <= n)
        m9 = max(i for i in list9 if i <= n)
        l6 = n - m6
        l9 = n - m9
        m[n] = min(ans(l6)+1,ans(l9)+1)
        return m[n]
print(ans(n))