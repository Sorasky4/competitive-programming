def cmb(n,r):
    a = 1
    b = 1
    for i in range((n-r+1),n+1):
        a *= i
    for i in range(1,r+1):
        b *= i
    ans = a/b
    return ans

